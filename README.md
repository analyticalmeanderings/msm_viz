# Practice Medicine Supply Map Case Study

## About this app

This open-ended, free-form case study prepares.

Data are downloaded from ...  
This dataset covers ...

No data dictionaries, we are in startup land

## How to run this app.py locally

To run this app locally, clone this repository and open this app folder in your terminal/Command Prompt. We suggest you to create a virtual environment for installation of required packages for this app.

```
cd dash-medical-provider-charges
python3 -m virtualenv venv

```
In Unix System:
```
source venv/bin/activate

```

In Windows: 

```
venv\Scripts\activate
```

Install all required packages by running:
```
pip install -r requirements.txt
```

Run this app locally by:
```
python app.py
```

## How to use this app

Select state, cost metric and region to visualize average charges or payments(for all medical procedures) on the map. Click on individual hospital from map to highlight its procedure-specific charges on the bottom chart. You may also click or select individual data from bottom plot to view its geological location, as well as charges/payment summaries from datatable.

## Screenshot

![Screencast](screenshot.png)

## Resources
* [Dash](https://dash.plot.ly/)
* Inspired by [this set of websites](https://dash-gallery.plotly.host/Portal/)
