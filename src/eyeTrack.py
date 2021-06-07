# import tobii_research as tr
from tobiiresearch.implementation.EyeTracker import EYETRACKER_GAZE_DATA
from tobiiresearch.interop import interop

import time
import csv
data_list = []

def gaze_data_callback(gaze_data):
    # print gaze points of left and right eye
    tmp = []
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))
    # time stamp
    timestamp = int(interop.get_system_time_stamp())

    tmp.apend(timestamp)
    # left gaze point
    tmp.append(gaze_data['left_gaze_point_on_display_area'])
    # right gaze point
    tmp.append(gaze_data['right_gaze_point_on_display_area'])
    # store into data list
    data_list.append(tmp)


if __name__ == '__main__':
    found_eyeTracker = interop.find_all_eyetrackers()
    device_num = len(found_eyeTracker)
    print('{} trackers detected'.format(device_num))
    try:
        if device_num <= 0:
            raise Exception('no device detected')
    except Exception as e:
        print(e)
        exit(-1)

    vive_tracker = found_eyeTracker[0]
    # # 获取gaze输出的频率
    # frequencyRes = interop.get_gaze_output_frequency(vive_tracker)
    # # set frequency
    # interop.set_gaze_output_frequency(vive_tracker,frequencyRes[0])

    print("Address: " + vive_tracker.address)
    print("Model: " + vive_tracker.model)
    print("Name: " + vive_tracker.device_name)
    print("Serial number: " + vive_tracker.serial_number)

    vive_tracker.subscribe_to(EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    # stop collecting gaze data
    vive_tracker.unsubscribe_from(EYETRACKER_GAZE_DATA, gaze_data_callback)

    # spare some time for displaying
    time.sleep(10)

    with open('../data/eyeData.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'left gaze point', 'right gaze point'])
        writer.writerows(data_list)
