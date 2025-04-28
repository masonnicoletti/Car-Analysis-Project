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
    
    #dropping rows with unnecessary data
    df = df[~df['model'].str.lower().isin(['door', 'doors'])]
    df = df[df['country'].str.lower() != 'canada']
    df = df[df['brand'].str.lower() == 'ford']
    df = df[df['mileage'] <= 150000]
    df = df[df['year'] >= 2010]

    #creating a new column for car age
    df['age'] = 2020 - df['year']

    # converting model to binary to check for f-150
    df['is_f-150'] = df['model'].apply(lambda x: 1 if x == 'f-150' else 0)

    # Drop unnecessary columns
    df = df.drop(columns=['condition', 'title_status', 'id', 'state', 'vin', 'lot', 'country', 'brand', 'year', 'model'], errors='ignore')
    
    # Collapse color
    main_colors = ['white', 'black', 'gray', 'silver', 'red', 'blue']
    df['color'] = df['color'].str.lower().apply(lambda x: x if any(color in x for color in main_colors) else 'other')
    
    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype('category')

    return df
