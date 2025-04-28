## data cleaning
import pandas as pd

def clean_car_data(df):
    # regions
    region_mapping = {
        'Northeast': ['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA'],
        'Midwest': ['IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'],
        'South': ['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'DC', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'],
        'West': ['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY', 'AK', 'CA', 'HI', 'OR', 'WA']
    }
    # Reverse the region mapping to state -> region
    state_to_region = {state: region for region, states in region_mapping.items() for state in states}
    df['region'] = df['state'].map(state_to_region)
    
    # Drop unnecessary columns
    df = df.drop(columns=['condition', 'title_status', 'id', 'state'], errors='ignore')
    
    # Collapse color
    main_colors = ['white', 'black', 'gray', 'silver', 'red', 'blue']
    df['color'] = df['color'].str.lower().apply(lambda x: x if any(color in x for color in main_colors) else 'other')
    
    return df