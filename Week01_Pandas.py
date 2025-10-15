# Nama : Alex simon sianturi 
# NRP  : 2473036
# pandas 

#Video1(Prefix & suffix pada kolom pandas data frame)
#Menyatakan Prefix dan SuFixx pada Kolom data frame

#Import Modules
import pandas as pd 
import numpy as np

print(pd.__version__)
print(nd.__version__)

#Persiapan Data Frame

n_crows = 3
n_cols  = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1,10, size=(n_rows, n_cols)),colums=cols)
df
tuple('ABCDE')

#Menyertakan Prefix kolom
df.add_prefix('kolom')

#Menyertakan Suffix Kolom
df.add_suffix('_field')

#Video 2 (seleksi baris pada pandas data frame)
#Pemilihan baris (rows selection) pada data frame

#Persiapan data Frame
n_crows = 10
n_cols  = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1,5, size=(n_rows, n_cols)),colums=cols)
df

# selection dengan operator logika |
df[(df['A'] == 1) | (df['A'] == 3)]

#selection demgan fungsi isin()
df[df['A'].isin([1, 3])]

#Mengenal operator negasi ~
df[~df['A+'].isin([1, 3])]

#Video03( Konversi tipe data numerik pada pandas data frame)
#Konversi tipe data string ke numerik pada kolom data Frame

#Menginmport Modules 
import pandas as pd

print(pd.__version__)

#mempersiapkan data frame
data ={'col1':['1','2','3','teks'],'col2':['1','2','3','4']}

df = pd.DataFrame(data)
df
df.dtypes

#konversi tipe data fungsi astype()
df_x = df.astype({'col2':'int'})
df_x

df_x.dytpes

#konversi tipe data numerik dengan fungsi to_numeric()
df.apply(pd.to_numeric, erros='coerce')

#Video04( Seleksi kolom pada data frame berdasarkan tipe data)
#import modules
import pandas as pd 
import numpy as np

print(pd.__version__)
print(nd.__version__)

#persiapan data frame 
n_rows = 5
n_cols = 2
cols = ['bil_pecahan', 'bil_bulat']

df = pd.Dataframe(np.random.randint(1, 20 size=(n_rows, n_cols)),colums=cols)
df ['bil_pecahan'] = df['bil_pecahan'].astype{'float'}
df.index = pd.util.testing.makeDataIndex(n_rows, freq='H')
df = df.reset_index{ }

df['teks']=list{'ABCDE'}

df

df.dytpes

#memilih kolom bertipe data numerik
df.select_dtypes{include='number'}
#memilih kolom bertipe data float 
df.select_dtypes{include='float'}
#memilih kolom bertipe data integr
df.select_dtypes{include='int'}
#memilih kolom bertipe data string atau object
df.select_dtypes{include='object'}
#memilih kolom bertipe data datetime
df.select_dtypes{include='odatetime'}
#memilih kolom dengan kombinasi tipe data
df.select_dtypes{include=['number','object']}