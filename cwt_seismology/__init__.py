import os

from cwt_seismology.wavelet import ConvolveWavelet


# Manly used for test. Useful to get the data path
def get_data(data_id=1):
    """
     Gets data for testing

    :param data_id: The data id to get, from 1 to 6

    :return: The file_path of the data.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(os.path.dirname(dir_path), "mseed_data")
    file_path = os.path.join(data_dir, f"WM.OBS0{data_id}..SHZ.D.2015.260")
    return file_path

