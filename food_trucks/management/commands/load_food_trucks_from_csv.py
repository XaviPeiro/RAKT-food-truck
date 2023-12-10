import logging
import os

from django.contrib.gis.geos import Point
from django.core.management import BaseCommand
import pandas as pd
from pandas import DataFrame

from food_trucks.models import FoodTruck

logger = logging.getLogger(__name__)

DIR = os.path.dirname(__file__)
APP_DIR = os.path.join(DIR, '../..')
DATA_DIR = os.path.join(APP_DIR, 'data')
TRUCK_FOOD_INIT_DATA_FILE = os.path.join(DATA_DIR, 'init-food-truck-data.csv')


class Command(BaseCommand):
    help = 'Load FoodTrucks from a CSV file into the database'

    def add_arguments(self, parser):
        # TODO: make this optional w TRUCK_FOOD_INIT_DATA_FILE as default
        # parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        ...

    def handle(self, *args, **kwargs):
        csv_file = TRUCK_FOOD_INIT_DATA_FILE
        self.load_data(csv_file)

    def load_data(self, csv_file: str):
        with open(csv_file, 'r') as file:
            df = pd.read_csv(file)
            entry = {}
            valid_food_trucks_df = self.get_valid_food_trucks(df=df)
            # Iterate through rows and save to the database
            for _, food_truck in valid_food_trucks_df.iterrows():
                entry["id"] = food_truck["permit"]
                entry["name"] = food_truck['Applicant']
                entry["latitude_longitude_geo"] = Point(x=food_truck['Longitude'], y=food_truck['Latitude'])
                entry["food_description"] = food_truck['FoodItems']
                entry["address"] = food_truck['LocationDescription']

                # Create and save the Django model instance
                FoodTruck.objects.create(**entry)
                entry = {}

    @staticmethod
    def get_valid_food_trucks(df: DataFrame) -> DataFrame:
        df_without_duplicated_food_trucks = df.drop_duplicates(subset='permit')
        df_without_duplicated_food_trucks_and_approved_permit = df_without_duplicated_food_trucks[
            df_without_duplicated_food_trucks['Status'] == 'APPROVED'
        ]

        return df_without_duplicated_food_trucks_and_approved_permit

