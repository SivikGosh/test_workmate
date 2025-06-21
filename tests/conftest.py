import csv
import os
import tempfile
from argparse import ArgumentParser
from parser.commands import Row

import pytest


@pytest.fixture
def parser():
    return ArgumentParser()


@pytest.fixture
def command(parser, command_class):
    return command_class(parser)


@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile(
        'w+',
        newline='',
        delete=False,
        encoding='utf-8'
    ) as tmp:
        writer = csv.writer(tmp)
        writer.writerow(['name', 'brand', 'brandprice', 'rating'])
        writer.writerow(['iphone 15 pro', 'apple', '999', '4.9'])
        writer.writerow(['galaxy s23 ultra', 'samsung', '1199', '4.8'])
        writer.writerow(['redmi 10c', 'xiaomi', '149', '4.1'])
        path = tmp.name
    yield path
    os.remove(path)


@pytest.fixture
def headers():
    headers = ['name', 'brand', 'brandprice', 'rating']
    return headers


@pytest.fixture
def rows():
    rows = [
        Row(
            name='iphone 15 pro',
            brand='apple',
            brandprice='999',
            rating='4.9'
        ),
        Row(
            name='galaxy s23 ultra',
            brand='samsung',
            brandprice='1199',
            rating='4.8'
        ),
        Row(
            name='redmi 10c',
            brand='xiaomi',
            brandprice='149',
            rating='4.1'
        ),
    ]
    return rows


@pytest.fixture
def filtered_row():
    return [Row(
        name='redmi 10c',
        brand='xiaomi',
        brandprice='149',
        rating='4.1'
    )]


@pytest.fixture
def filtered_max_price_row():
    return [Row(
        name='galaxy s23 ultra',
        brand='samsung',
        brandprice='1199',
        rating='4.8'
    )]


@pytest.fixture
def filtered_max_rating_row():
    return [Row(
        name='iphone 15 pro',
        brand='apple',
        brandprice='999',
        rating='4.9'
    )]


@pytest.fixture
def asc_name_rows():
    rows = [
        Row(
            name='galaxy s23 ultra',
            brand='samsung',
            brandprice='1199',
            rating='4.8'
        ),
        Row(
            name='iphone 15 pro',
            brand='apple',
            brandprice='999',
            rating='4.9'
        ),
        Row(
            name='redmi 10c',
            brand='xiaomi',
            brandprice='149',
            rating='4.1'
        ),
    ]
    return rows


@pytest.fixture
def desc_name_rows():
    rows = [
        Row(
            name='redmi 10c',
            brand='xiaomi',
            brandprice='149',
            rating='4.1'
        ),
        Row(
            name='iphone 15 pro',
            brand='apple',
            brandprice='999',
            rating='4.9'
        ),
        Row(
            name='galaxy s23 ultra',
            brand='samsung',
            brandprice='1199',
            rating='4.8'
        ),
    ]
    return rows


@pytest.fixture
def asc_brand_rows():
    rows = [
        Row(
            name='iphone 15 pro',
            brand='apple',
            brandprice='999',
            rating='4.9'
        ),
        Row(
            name='galaxy s23 ultra',
            brand='samsung',
            brandprice='1199',
            rating='4.8'
        ),
        Row(
            name='redmi 10c',
            brand='xiaomi',
            brandprice='149',
            rating='4.1'
        ),
    ]
    return rows


@pytest.fixture
def desc_brand_rows():
    rows = [
        Row(
            name='redmi 10c',
            brand='xiaomi',
            brandprice='149',
            rating='4.1'
        ),
        Row(
            name='galaxy s23 ultra',
            brand='samsung',
            brandprice='1199',
            rating='4.8'
        ),
        Row(
            name='iphone 15 pro',
            brand='apple',
            brandprice='999',
            rating='4.9'
        ),
    ]
    return rows
