# -*- coding: utf-8 -*-

import pydicom
import os
import sys
"""
@author yaoxs@shukun.net
@date 2019/11/15 18:22
"""


def find_dicom(file_path):
    if os.path.isdir(file_path):
        dir_files = os.listdir(file_path)
        for dicom in dir_files:
            dicom = os.path.join(file_path, dicom)
            print_dicom_meta(dicom)
    else:
        print_dicom_meta(file_path)


def print_dicom_meta(dcm_file):
    if os.path.splitext(dcm_file)[1] == '.dcm':
        dcm_meta = pydicom.read_file(dcm_file)
        order = dcm_meta.get("InstanceNumber")
        series_uid = dcm_meta.get("SeriesInstanceUID")
        study_uid = dcm_meta.get("StudyInstanceUID")
        print("dcm order: %d, series_uid: %s, study_uid: %s" % (order, series_uid, study_uid))
    else:
        print("Not dcm file: %s" % dcm_file)


if __name__ == '__main__':
    path = sys.argv[1]
    find_dicom(path)