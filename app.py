# remember to check default values... 
import streamlit as st
import joblib
import numpy as np

model = joblib.load('housing_gb.pkl')

st.title('Ames house price prediction')

names = ['Lot area (sq ft)', 'Overall quality', 'Overall condition', 
        'Year built', 'Year remodelled', 'Masonry veneer area',
        'Basement finished sq ft', 'Basement unfinished sq ft',
        '1st floor sq ft', '2nd floor sq ft', 'Above grade sq ft',
        'Basement full baths', 'Full baths above grade',
        'Half baths above grade', 'Bedrooms above grade',
        'Total rooms (not bathrooms) above grade',
        'Fireplaces', 'Garage year built', 'Garage cars',
        'Garage area (sq ft)', 'Wood deck sq ft', 'Open porch sq ft',
        'Month sold', 'Year sold']
mins = [1000, 1, 1, 1879, 1950, 0, 0, 400, 0, 400, 0, 0, 0, 0, 0, 0, 0,
        1895, 0, 0, 0, 0, 1, 2006]
maxs = [100000, 10, 10, 2010, 2010, 1600, 5700, 2400, 5100, 2100, 5700, 2,
        4, 2, 6, 15, 4, 2010, 4, 1500, 1500, 600, 12, 2010]
values = [10000, 6, 6, 1972, 1985, 0, 400, 480, 1091, 0, 1450, 0, 1, 0,
          3, 6, 1, 1979, 2, 482, 0, 28, 6, 2008]
predictors = []

n = len(names)
for i in range(n):
    predictors.append(st.slider(names[i], mins[i], maxs[i], values[i]))
    
predictors.insert(8, predictors[6] + predictors[7])    
to_transf = [0, 5, 6, 8, 9, 11, 21, 22]
for i in to_transf:
    predictors[i] = np.log1p(predictors[i])

ms_subclass = st.selectbox('MS Subclass',
    options = ['1-STORY 1946 & NEWER ALL STYLES',
               '1-1/2 STORY FINISHED ALL AGES',
               '2-STORY 1946 & NEWER',
               'Other'], index = 0)
if ms_subclass == '1-STORY 1946 & NEWER ALL STYLES':
    predictors.extend([True, False, False])
elif ms_subclass == '1-1/2 STORY FINISHED ALL AGES':
    predictors.extend([False, True, False])
elif ms_subclass == '2-STORY 1946 & NEWER':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False])

ms_zoning = st.selectbox('MS Zoning',
    options = ['Residential Low Density',
               'Residential Medium Density',
               'Other'], index = 1)
if ms_zoning == 'Residential Low Density':
    predictors.extend([True, False])
elif ms_zoning == 'Residential Medium Density':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])               

lot_shape = st.selectbox('Lot shape',
    options = ['Regular',
               'Slightly irregular',
               'Moderately irregular or irregular'], index = 0)
if lot_shape == 'Slightly irregular':
    predictors.extend([True, False])
elif lot_shape == 'Regular':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])  

lot_contour = st.checkbox('Near flat/level property', value = True) 
predictors.append(lot_contour)

lot_config = st.selectbox('Lot configuration',
    options = ['Inside lot',
               'Corner lot',
               'Other'], index = 0)
if lot_config == 'Corner lot':
    predictors.extend([True, False])
elif lot_config == 'Inside lot':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])  

nbhd = st.selectbox('Neighborhood',
    options = ['College Creek',
               'North Ames',
               'Other'], index = 2)
if nbhd == 'College Creek':
    predictors.extend([True, False])
elif nbhd == 'North Ames':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])                

cond1 = st.checkbox('Near arterial street, feeder street, railroad, etc.', 
    value = False)  
predictors.append(cond1)

bldg_type = st.checkbox('Single-family detached home', value = True) 
predictors.append(bldg_type)
  
if ms_subclass == '1-STORY 1946 & NEWER ALL STYLES':
    predictors.extend([False, True, False])
elif ms_subclass == '1-1/2 STORY FINISHED ALL AGES':
    predictors.extend([True, False, False])
elif ms_subclass == '2-STORY 1946 & NEWER':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False])  

roof_style = st.selectbox('Roof style',
    options = ['Gable',
               'Hip',
               'Other'], index = 0)   
if roof_style == 'Gable':
    predictors.extend([True, False])
elif roof_style == 'Hip':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])   
               
ext1 = st.selectbox('Exterior covering',
    options = ['Hard board',
               'Metal siding',
               'Vinyl siding',
               'Wood siding',
               'Other'], index = 2)
if ext1 == 'Hard board':
    predictors.extend([True, False, False, False])
elif ext1 == 'Metal siding':
    predictors.extend([False, True, False, False])
elif ext1 == 'Vinyl siding':
    predictors.extend([False, False, True, False])
elif ext1 == 'Wood siding':
    predictors.extend([False, False, False, True])
else:
    predictors.extend([False, False, False, False])
               
ext2 = st.selectbox('Exterior covering (if more than one material)',
    options = ['Hard board',
               'Metal siding',
               'Vinyl siding',
               'Wood siding',
               'Other'], index = 2)
if ext2 == 'Hard board':
    predictors.extend([True, False, False, False])
elif ext2 == 'Metal siding':
    predictors.extend([False, True, False, False])
elif ext2 == 'Vinyl siding':
    predictors.extend([False, False, True, False])
elif ext2 == 'Wood siding':
    predictors.extend([False, False, False, True])
else:
    predictors.extend([False, False, False, False])               

ext_qual = st.select_slider('Exterior quality',
                ['Poor', 'Fair', 'Typical/Average', 'Good', 'Excellent'],
                value = 'Typical/Average')
if ext_qual == 'Good':
    predictors.extend([True, False])
elif ext_qual == 'Typical/Average':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])  
                
ext_cond = st.select_slider('Exterior condition',
                ['Poor', 'Fair', 'Typical/Average', 'Good', 'Excellent'],
                value = 'Typical/Average')
if ext_cond == 'Good':
    predictors.extend([True, False])
elif ext_cond == 'Typical/Average':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])  
               
foundation = st.selectbox('Type of foundation',
    options = ['Brick & tile',
               'Cinder block',
               'Poured concrete',
               'Other'], index = 2)
if foundation == 'Brick & tile':
    predictors.extend([True, False, False])
elif foundation == 'Cinder block':
    predictors.extend([False, True, False])
elif foundation == 'Poured concrete':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False])

bsmt_qual = st.selectbox('Height of basement',
    options = ['100+ inches',
               '90-99 inches',
               '80-89 inches',
               '< 80 inches or no basement'], index = 2)
if bsmt_qual == '100+ inches':
    predictors.extend([True, False, False])
elif bsmt_qual == '90-99 inches':
    predictors.extend([False, True, False])
elif bsmt_qual == '80-89 inches':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False])               
               
bsmt_cond = st.checkbox('Typical basement condition (slight dampness allowed)',
            value = True)
predictors.append(bsmt_cond)            
            
bsmt_exp = st.selectbox('Basement exposure to walkout or garden level walls',
    options = ['Good exposure',
               'Average exposure',
               'Minimum exposure',
               'No exposure',
               'No basement'], index = 3)
if bsmt_exp == 'Average exposure':
    predictors.extend([True, False, False])
elif bsmt_exp == 'Good exposure':
    predictors.extend([False, True, False])
elif bsmt_exp == 'No exposure':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False])                 

bsmt_rating = st.selectbox('Rating of basement finished area',
    options = ['Good living quarters',
               'Average living quarters',
               'Below average living quarters',
               'Average rec room',
               'Unfinished',
               'Other or no basement'], index = 0)
if bsmt_rating == 'Average living quarters':
    predictors.extend([True, False, False, False, False])
elif bsmt_rating == 'Below average living quarters':
    predictors.extend([False, True, False, False, False])
elif bsmt_rating == 'Good living quarters':
    predictors.extend([False, False, True, False, False])
elif bsmt_rating == 'Average rec room':
    predictors.extend([False, False, False, True, False])
elif bsmt_rating == 'Unfinished':
    predictors.extend([False, False, False, False, True])
else:
    predictors.extend([False, False, False, False, False])
predictors.append(True)    

heat_qc = st.select_slider('Heating quality and condition',
                ['Poor', 'Fair', 'Typical/Average', 'Good', 'Excellent'],
                value = 'Excellent')
if heat_qc== 'Excellent':
    predictors.extend([True, False, False])
elif heat_qc == 'Good':
    predictors.extend([False, True, False])
elif heat_qc == 'Typical/Average':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False]) 
                
elec = st.checkbox('Standard circuit breakers and Romex',
            value = True) 
predictors.append(elec)            
            
kitchen_qual = st.select_slider('Kitchen quality',
                ['Poor', 'Fair', 'Typical/Average', 'Good', 'Excellent'],
                value = 'Typical/Average')
if kitchen_qual == 'Good':
    predictors.extend([True, False])
elif kitchen_qual == 'Typical/Average':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])  
                
garage_type = st.selectbox('Garage location',
    options = ['Attached to home',
               'Detached from home',
               'Other or no garage'], index = 0)  
if garage_type == 'Attached to home':
    predictors.extend([True, False])
elif garage_type == 'Detached from home':
    predictors.extend([False, True])
else:
    predictors.extend([False, False])  
               
garage_finish = st.select_slider('Interior finish of the garage',
                ['No garage', 'Unfinished', 'Rough finished', 'Finished'],
                value = 'Unfinished')
if garage_finish == 'Finished':
    predictors.extend([True, False, False])
elif garage_finish == 'Rough finished':
    predictors.extend([False, True, False])
elif garage_finish == 'Unfinished':
    predictors.extend([False, False, True])
else:
    predictors.extend([False, False, False])                

paved_driveway = st.checkbox('Paved driveway', value = True)
predictors.append(paved_driveway)

sale_type = st.checkbox('Warranty deed - conventional', value = True)
predictors.append(sale_type)

sale_cond = st.checkbox('Normal sale', value = True)
predictors.append(sale_cond)

prediction = np.exp(model.predict(np.array(predictors).reshape(1,-1))[0])
st.success(f'Prediction: ${prediction:,.2f}')

with st.sidebar:
    st.write("""Using the [Ames housing dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset),
    I trained various regression models to predict the sale price of a house.
    The best model was achieved with gradient boosting, giving an
    RMSE of 0.1091 for the log of the sale price. \n \n A more detailed 
    explanation of the variables can be found 
    [here](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt).
    """)
    

