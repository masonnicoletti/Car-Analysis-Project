## data cleaning function
def clean_car_data(df):
    df = df.copy()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Map full lowercase state names to regions
    region_mapping = {
        'Northeast': ['connecticut', 'maine', 'massachusetts', 'new hampshire', 'rhode island', 'vermont', 'new jersey', 'new york', 'pennsylvania'],
        'Midwest': ['illinois', 'indiana', 'michigan', 'ohio', 'wisconsin', 'iowa', 'kansas', 'minnesota', 'missouri', 'nebraska', 'north dakota', 'south dakota'],
        'South': ['delaware', 'florida', 'georgia', 'maryland', 'north carolina', 'south carolina', 'virginia', 'district of columbia', 'west virginia', 
                  'alabama', 'kentucky', 'mississippi', 'tennessee', 'arkansas', 'louisiana', 'oklahoma', 'texas'],
        'West': ['arizona', 'colorado', 'idaho', 'montana', 'nevada', 'new mexico', 'utah', 'wyoming', 'alaska', 'california', 'hawaii', 'oregon', 'washington']
    }
    state_to_region = {state: region for region, states in region_mapping.items() for state in states}
    
    if 'state' in df.columns:
        df['state'] = df['state'].str.lower()  # just in case it's not already lowercase
        df['region'] = df['state'].map(state_to_region)
        df['region'] = df['region'].fillna('other')
    else:
        df['region'] = 'other'
    
    # Drop unnecessary columns
    df = df[~df['model'].str.lower().isin(['door', 'doors'])]
    df = df[df['country'].str.lower() != 'canada']
    df = df.drop(columns=['condition', 'title_status', 'id', 'state', 'vin', 'lot', 'country'], errors='ignore')
    
    # Collapse color
    main_colors = ['white', 'black', 'gray', 'silver', 'red', 'blue']
    df['color'] = df['color'].str.lower().apply(lambda x: x if any(color in x for color in main_colors) else 'other')
    
    # Drop cars before 2010
    df = df[df['year'] >= 2010]
    
    return df