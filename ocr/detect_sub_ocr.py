import cv2
import numpy as np
import pytesseract
import os
import math
from pathlib import Path
import re
from difflib import SequenceMatcher
import pandas as pd
INPUT_DIR = "./"
OUTPUT_DIR = "./"
#first detect where the subtitle is 
#limit detection to this region 
################################## CV2 FUNCTIONS ########################
class CV2_HELPER:

    # Returns a binary image using an adaptative threshold
    def binarization_adaptative_threshold(self, image):
        # 11 => size of a pixel neighborhood that is used to calculate a threshold value for the pixel
        return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    def binarization_otsu(self, image):
        blur = cv2.GaussianBlur(image, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return thresh

    # smoothen the image by removing small dots/patches which have high intensity than the rest of the image
    def remove_noise(self, image):
        return cv2.medianBlur(image, 5)

    # get grayscale image
    def get_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # dilation
    def dilate(self, image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.erode(image, kernel, iterations=1)

    ################################## OCR PROCESSING ########################


class BOXES_HELPER():

    def get_organized_tesseract_dictionary(self, tesseract_dictionary):
        res = {}
        n_boxes = len(tesseract_dictionary['level'])

        # Organize blocks
        res['blocks'] = {}
        for i in range(n_boxes):
            if tesseract_dictionary['level'][i] == 2:
                res['blocks'][tesseract_dictionary['block_num'][i]] = {
                    'left': tesseract_dictionary['left'][i],
                    'top': tesseract_dictionary['top'][i],
                    'width': tesseract_dictionary['width'][i],
                    'height': tesseract_dictionary['height'][i],
                    'paragraphs': {}
                }

        # Organize paragraphs
        for i in range(n_boxes):
            if tesseract_dictionary['level'][i] == 3:
                res['blocks'][tesseract_dictionary['block_num'][i]]['paragraphs'][
                    tesseract_dictionary['par_num'][i]] = {
                    'left': tesseract_dictionary['left'][i],
                    'top': tesseract_dictionary['top'][i],
                    'width': tesseract_dictionary['width'][i],
                    'height': tesseract_dictionary['height'][i],
                    'lines': {}
                }

        # Organize lines
        for i in range(n_boxes):
            if tesseract_dictionary['level'][i] == 4:
                res['blocks'][tesseract_dictionary['block_num'][i]]['paragraphs'][tesseract_dictionary['par_num'][
                    i]]['lines'][tesseract_dictionary['line_num'][i]] = {
                    'left': tesseract_dictionary['left'][i],
                    'top': tesseract_dictionary['top'][i],
                    'width': tesseract_dictionary['width'][i],
                    'height': tesseract_dictionary['height'][i],
                    'words': {}
                }

        # Organize words
        for i in range(n_boxes):
            if tesseract_dictionary['level'][i] == 5:
                res['blocks'][tesseract_dictionary['block_num'][i]]['paragraphs'][
                    tesseract_dictionary['par_num'][
                        i]]['lines'][tesseract_dictionary['line_num'][i]]['words'][tesseract_dictionary['word_num'][i]] \
                    = {
                    'left': tesseract_dictionary['left'][i],
                    'top': tesseract_dictionary['top'][i],
                    'width': tesseract_dictionary['width'][i],
                    'height': tesseract_dictionary['height'][i],
                    'text': tesseract_dictionary['text'][i],
                    'conf': float(tesseract_dictionary['conf'][i]),
                }

        return res

    def get_lines_with_words(self, organized_tesseract_dictionary):
        res = []
        for block in organized_tesseract_dictionary['blocks'].values():
            for paragraph in block['paragraphs'].values():
                for line in paragraph['lines'].values():
                    if 'words' in line and len(line['words']) > 0:
                        currentLineText = ''
                        for word in line['words'].values():
                            if word['conf'] > 60.0 and not word['text'].isspace():
                                currentLineText += word['text'] + ' '
                        if currentLineText != '':
                            res.append(
                                {'text': currentLineText, 'left': line['left'], 'top': line['top'], 'width': line[
                                    'width'], 'height': line[
                                    'height']})

        return res

    def show_boxes_lines(self, d, frame):
        text_vertical_margin = 12
        organized_tesseract_dictionary = self.get_organized_tesseract_dictionary(d)
        lines_with_words = self.get_lines_with_words(organized_tesseract_dictionary)
        #print(lines_with_words)
        for line in lines_with_words:
            x = line['left']
            y = line['top']
            h = line['height']
            w = line['width']
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            frame = cv2.putText(frame,
                                text=line['text'],
                                org=(x, y - text_vertical_margin),
                                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                                fontScale=1,
                                color=(0, 255, 0),
                                thickness=2)
        return frame
#boxes here
    def show_boxes_words(self, d, frame):
        text_vertical_margin = 12
        n_boxes = len(d['level'])
        for i in range(n_boxes):
            if (int(float(d['conf'][i])) > 60) and not (d['text'][i].isspace()):  # Words
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, text=d['text'][i], org=(x, y - text_vertical_margin),
                                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), thickness=2)
        return frame

    def add_subtitle(self, d, frame):
        text_vertical_margin = 12
        n_boxes = len(d['level'])
        for i in range(n_boxes):
            if (int(float(d['conf'][i])) > 60) and not (d['text'][i].isspace()):  # Words
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, text=d['text'][i], org=(x, y - text_vertical_margin),
                                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), thickness=2)
        return frame
class OCR_HANDLER:

    def __init__(self, video_filepath, cv2_helper, ocr_type="WORDS"):
        # The video_filepath's name with extension
        self.video_filepath = video_filepath
        self.cv2_helper = cv2_helper
        self.ocr_type = ocr_type
        self.boxes_helper = BOXES_HELPER()
        self.video_name = Path(self.video_filepath).stem
        self.frames_folder = OUTPUT_DIR + 'temp/' + self.video_name + '_frames'
        self._fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change to 'MP4V' if this doesn't work on your OS.
        self.out_extension = '.mp4'
        self.out_name = self.video_name + '_boxes' + self.out_extension
        self.sublist = []
        self.x, self.y, self.w, self.h = 0,0,1000,1000

    ########## EXTRACT FRAMES AND FIND WORDS #############
    #important stuff here
    def process_frames(self):

        frame_name = './' + self.frames_folder + '/' + self.video_name + '_frame_'

        if not os.path.exists(self.frames_folder):
            os.makedirs(self.frames_folder)

        video = cv2.VideoCapture(self.video_filepath)
        self.fps = round(video.get(cv2.CAP_PROP_FPS))  # get the FPS of the video_filepath
        #this data is sorta important
        frames_durations, frame_count = self.get_saving_frames_durations(video, self.fps)  # list of point to save

        print("SAVING VIDEO:", frame_count, "FRAMES AT", self.fps, "FPS")

        idx = 0
        #x,y,w,h = 100,500,900,300
        print(":", end='', flush=True)
        while True:
            print("=", end='', flush=True)
            is_read, frame = video.read()
            if not is_read:  # break out of the loop if there are no frames to read
                break
            frame_duration = idx / self.fps
            try:
                # get the earliest duration to save
                closest_duration = frames_durations[0]
            except IndexError:
                # the list is empty, all duration frames were saved
                break
            if frame_duration >= closest_duration:
                # if closest duration is less than or equals the frame duration, then save the frame
                output_name = frame_name + str(idx) + '.png'
                #here is where we make the modification to cut the frame into specific parts

                #first find region of interest within the first 5% frames, and apply region of interest to the rest of the video
                # crop_frame = frame[y:y+h, x:x+w]
                # return crop_frame
                """                
                if idx == 30:
                    frame = self.cv2_helper.binarization_otsu(self.cv2_helper.get_grayscale(frame))
                    x,y,w,h = cv2.boundingRect(frame)
                """
                crop_frame = frame[self.y:self.y+self.h, self.x:self.x+self.w]
                frame, sub = self.ocr_frame(crop_frame)
                cv2.imwrite(output_name, frame)
                #get subtitle data
                self.sublist.append((idx,sub))

                if (idx % 10 == 0) and (idx > 0):
                    print(">")
                    print("Saving frame: ..." + output_name)
                    print(":", end='', flush=True)
                # drop the duration spot from the list, since this duration spot is already saved
                try:
                    frames_durations.pop(0)
                except IndexError:
                    pass
            # increment the frame count
            idx += 1
        if (idx - 1 % 10 != 0):
            print(">")
        print("\nSaved and processed", idx, "frames")
        video.release()

    def assemble_video(self):
        #not important, only video assembly
        print("ASSEMBLING NEW VIDEO")

        images = [img for img in os.listdir(self.frames_folder) if img.endswith(".png")]  # Careful with the order
        images = sorted(images, key=lambda x: float((x.split("_")[-1])[:-4]))

        frame = cv2.imread(os.path.join(self.frames_folder, images[0]))
        height, width, layers = frame.shape
        #key stuff here, frame.shape
        # half = height//2
        # top = frame[:half, :]
        video = cv2.VideoWriter(OUTPUT_DIR + self.out_name, self._fourcc, self.fps, (width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(self.frames_folder, image)))

        video.release()

        # When finished, delete all frames stored temporarily on disk.
        for f in os.listdir(self.frames_folder):
            if not f.endswith(".png"):
                continue
            try:
                os.remove(os.path.join(self.frames_folder, f))
            except OSError as e:
                print("Error: %s : %s" % (self.frames_folder, e.strerror))

        # Then delete the directory that contained the frames.
        try:
            os.rmdir(self.frames_folder)
        except OSError as e:
            print("Error: %s : %s" % (self.frames_folder, e.strerror))

    def get_saving_frames_durations(self, video, saving_fps):
        """A function that returns the list of durations where to save the frames"""
        s = []
        # get the clip duration by dividing number of frames by the number of frames per second
        clip_duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
        # use np.arange() to make floating-point steps
        for i in np.arange(0, clip_duration, 1 / saving_fps):
            s.append(i)
        return s, video.get(cv2.CAP_PROP_FRAME_COUNT)

    def ocr_frame(self, frame):

        im, d = self.compute_best_preprocess(self.cv2_helper.get_grayscale(frame))

        #function to remove blank space in d
        try:
            raw_text=d['text']
        except TypeError:
            raw_text = ['']

        text = [t for t in raw_text if t != '' and len(t) > 1 or t == 'I']
        for i in range (len(text)):
             text[i]=re.sub(r'[\W_]+', '', text[i])
        joined = ' '.join(text)

        """
        for index in d:
            index = [pos for pos in index if index != 1]
            pass
        """
        try:
            if (self.ocr_type == "LINES"):
                frame = self.boxes_helper.show_boxes_lines(d, frame)
            else:
                #for subtitles ocr type should just be lines
                frame = self.boxes_helper.show_boxes_words(d, frame)
        except Exception:
            pass
        return frame, joined

    def compute_best_preprocess(self, frame):
        def f(count, mean):
            return 10 * count + mean

        best_f = 0
        best_opt = 0
        best_im = frame
        best_d = None
        options = [["binarization1"],["binarization2"],["binarization2","remove_noise","dilate"]]

        for idx, opt in enumerate(options):
            # Apply preprocess
            im = frame
            if "binarization1" in opt:
                im = self.cv2_helper.binarization_adaptative_threshold(im)
            if "binarization2" in opt:
                im = self.cv2_helper.binarization_otsu(im)
            if "remove_noise" in opt:
                im = self.cv2_helper.remove_noise(im)
            if "dilate" in opt:
                im = self.cv2_helper.dilate(im)

            # Compute mean conf:
            #pytesseract is important here
            #use the config argument
            d = pytesseract.image_to_data(im, output_type=pytesseract.Output.DICT)
            #s = pytesseract.image_to_string(im, output_type=pytesseract.Output.DICT)
            confs = [int(float(d['conf'][i])) for i in range(len(d['text'])) if not (d['text'][i].isspace())]
            confs = [i for i in confs if i > 60]

            mean_conf = np.asarray(confs).mean() if len(confs) > 0 else 0

            #print(len(confs),mean_conf,f(len(confs),mean_conf))

            if f(len(confs), mean_conf) > best_f:
                best_im = im
                best_d = d
                best_f = f(len(confs), mean_conf)
                #print(opt)

        return best_im, best_d


    def sort_list(self):
        list = self.sublist
        j=0
        masterlist = []
        for i in range(len(list)):

            #print(j)
            frame = list[i][0]
            sub = list[i][1]
        
            similarity = SequenceMatcher(None, sub, list[j][1]).ratio()

            if similarity <=0.40:
                time_tuple=(j/self.fps,frame/self.fps)
                sub_list = [list[j+k][1] for k in range(i-j)]
                masterlist.append((time_tuple, sub_list))
                j=frame
            elif i == len(list)-1:
                time_tuple=(j/self.fps,frame/self.fps)
                sub_list = [list[j+k][1] for k in range(i-j+1)]
                masterlist.append((time_tuple, sub_list))

        self.sublist = masterlist

    def find_best_sub(self):
        l = self.sublist
        masterlist = []
        for i in range(len(l)):
            df = pd.Series(l[i][1]).astype(str)
            count = df.value_counts()
            sub = list(count.head().index)[0]
            new_tuple = (l[i][0],sub)
            masterlist.append(new_tuple)
        self.sublist = masterlist
        return masterlist




#final func
def detect(filename, ocr_type):
    if os.path.isfile(filename):
        ocr_handler = OCR_HANDLER(filename, CV2_HELPER(),ocr_type)
        ocr_handler.process_frames()
        ocr_handler.assemble_video()
        print("OCR PROCESS FINISHED: OUTPUT FILE => " + ocr_handler.out_name)

        print(ocr_handler.sublist)
        ocr_handler.sort_list()
        print(ocr_handler.find_best_sub())
        df = pd.Series(ocr_handler.sublist)
        df.to_csv(f'{OUTPUT_DIR}/{filename}.csv')
        #location = ocr_handler.calculate_location()

    else:
        print("FILE NOT FOUND: BYE")
#WORDS
detect('vid7.mp4','WORDS')