#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 16:23:42 2022

@author: Nishad Mandlik
"""

from getpass import getpass
from komPYoot import API, TourType, TourStatus, Sport, TourOwner

_DOWNLOAD_DIR = "./"


def main():
    print("Please enter your Komoot account credentials.")
    email_id = input("Email ID: ")
    password = getpass("Password (hidden input): ")

    a = API()
    a.login(email_id, password)

    # Get list of tours with the given filters
    tours = a.get_user_tours_list(tour_type=TourType.PLANNED,
                                  tour_status=TourStatus.PUBLIC,
                                  sport=Sport.BIKE_TOURING,
                                  tour_owner=TourOwner.SELF)

    # Get the ID of the first tour in the list
    tour_id = tours[0]["id"]

    # Download the tour to the specified directory
    file_name = a.download_tour_gpx(tour_id, _DOWNLOAD_DIR)

    # Upload the downloaded tour as an recorded activity
    a.upload_tour_gpx(Sport.BIKE_TOURING, _DOWNLOAD_DIR + "/" + file_name)

    return tours


if __name__ == '__main__':
    tours = main()
