import geopandas as gpd
# import pandas as pd

parcels_data = gpd.read_file(r'Township_template.shp')

# townships_nums = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
# ranges_nums = [28, 30, 31, 32, 33, 34, 35, 36, 37]

# township_condition = parcels_data['Township'].isin(townships_nums)
# range_condition = parcels_data['Range'].isin(ranges_nums)

# parcels_data = parcels_data[township_condition & range_condition]


########1
condition1 = parcels_data[(parcels_data['Township'] == 1) & (parcels_data['Range'] == 36)]
section1 = condition1[condition1['Section'] == 24]


########2
condition2 = parcels_data[(parcels_data['Township'] == 2) & (parcels_data['Range'] == 36)]
section2 = condition2[condition2['Section'] == 23]


#########17
condition3 = parcels_data[(parcels_data['Township'] == 17) & (parcels_data['Range'] == 35)]
section3 = condition3[condition3['Section'].isin([2, 3, 4, 10, 11])]

condition4 = parcels_data[(parcels_data['Township'] == 17) & (parcels_data['Range'] == 36)]
section4 = condition4[condition4['Section'].isin([2, 3, 4, 9, 10])]


########18
condition5 = parcels_data[(parcels_data['Township'] == 18) & (parcels_data['Range'] == 34)]
section5 = condition5[condition5['Section'].isin([16, 7])]

condition6 = parcels_data[(parcels_data['Township'] == 18) & (parcels_data['Range'] == 35)]
section6 = condition6[condition6['Section'].isin([14, 23, 25, 26, 27, 31, 32, 33, 34, 35])]

condition7 = parcels_data[(parcels_data['Township'] == 18) & (parcels_data['Range'] == 36)]
section7 = condition7[condition7['Section'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 22, 23, 26, 27, 33, 34])]

condition8 = parcels_data[(parcels_data['Township'] == 18) & (parcels_data['Range'] == 37)]
section8 = condition8[condition8['Section'] == 6]


#########19
condition9 = parcels_data[(parcels_data['Township'] == 19) & (parcels_data['Range'] == 34)]
section9 = condition9[condition9['Section'].isin([5, 6, 24, 25, 31])]

condition10 = parcels_data[(parcels_data['Township'] == 19) & (parcels_data['Range'] == 35)]
section10 = condition10[condition10['Section'].isin([2, 4, 5, 8, 9, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25])]

condition11 = parcels_data[(parcels_data['Township'] == 19) & (parcels_data['Range'] == 36)]
section11 = condition11[condition11['Section'].isin([1, 6, 13, 18, 19, 20, 21, 28, 29, 30, 31, 32, 33, 34, 35])]

condition12 = parcels_data[(parcels_data['Township'] == 19) & (parcels_data['Range'] == 37)]
section12 = condition12[condition12['Section'].isin([6, 19, 30])]


#########20
condition13 = parcels_data[(parcels_data['Township'] == 20) & (parcels_data['Range'] == 33)]
section13 = condition13[condition13['Section'].isin([12, 13])]

condition14 = parcels_data[(parcels_data['Township'] == 20) & (parcels_data['Range'] == 34)]
section14 = condition14[condition14['Section'].isin([1, 2, 7, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31])]

condition15 = parcels_data[(parcels_data['Township'] == 20) & (parcels_data['Range'] == 35)]
section15 = condition15[condition15['Section'].isin([1, 2, 3, 5, 6, 7, 8, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33, 34])]

condition16 = parcels_data[(parcels_data['Township'] == 20) & (parcels_data['Range'] == 36)]
section16 = condition16[condition16['Section'].isin([1, 3, 5, 8, 9, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 24, 26, 27, 28, 29, 31, 32, 33])]

condition17 = parcels_data[(parcels_data['Township'] == 20) & (parcels_data['Range'] == 37)]
section17 = condition17[condition17['Section'].isin([6, 7, 18, 19, 30, 31])]


#########21
condition18 = parcels_data[(parcels_data['Township'] == 21) & (parcels_data['Range'] == 34)]
section18 = condition18[condition18['Section'].isin([23, 24, 25, 26, 27, 28, 33, 34, 35])]

condition19 = parcels_data[(parcels_data['Township'] == 21) & (parcels_data['Range'] == 35)]
section19 = condition19[condition19['Section'].isin([15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])]

condition20 = parcels_data[(parcels_data['Township'] == 21) & (parcels_data['Range'] == 36)]
section20 = condition20[condition20['Section'].isin([8, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 335])]

condition21 = parcels_data[(parcels_data['Township'] == 21) & (parcels_data['Range'] == 37)]
section21 = condition21[condition21['Section'].isin([7, 18, 19, 30])]

condition22 = parcels_data[(parcels_data['Township'] == 21) & (parcels_data['Range'] == 3)]
section22 = condition22[condition22['Section'] == 11]


#########22
condition23 = parcels_data[(parcels_data['Township'] == 22) & (parcels_data['Range'] == 34)]
section23 = condition23[condition23['Section'].isin([11, 12, 13, 14, 15, 21, 22, 23])]

condition24 = parcels_data[(parcels_data['Township'] == 22) & (parcels_data['Range'] == 35)]
section24 = condition24[condition24['Section'] == 6]

condition25 = parcels_data[(parcels_data['Township'] == 22) & (parcels_data['Range'] == 36)]
section25 = condition25[condition25['Section'].isin([27, 28, 34])]


#########23
condition26 = parcels_data[(parcels_data['Township'] == 23) & (parcels_data['Range'] == 28)]
section26 = condition26[condition26['Section'] == 36]

condition27 = parcels_data[(parcels_data['Township'] == 23) & (parcels_data['Range'] == 29)]
section27 = condition27[condition27['Section'] == 31]

condition28 = parcels_data[(parcels_data['Township'] == 23) & (parcels_data['Range'] == 31)]
section28 = condition28[condition28['Section'].isin([5, 6])]

condition29 = parcels_data[(parcels_data['Township'] == 23) & (parcels_data['Range'] == 34)]
section29 = condition29[condition29['Section'].isin([1, 2, 4, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 24, 25, 28])]

condition30 = parcels_data[(parcels_data['Township'] == 23) & (parcels_data['Range'] == 35)]
section30 = condition30[condition30['Section'].isin([7, 8, 17, 18, 19, 30, 31, 32])]

condition31 = parcels_data[(parcels_data['Township'] == 23) & (parcels_data['Range'] == 36)]
section31 = condition31[condition31['Section'].isin([22, 26, 27])]


#########24
condition32 = parcels_data[(parcels_data['Township'] == 24) & (parcels_data['Range'] == 29)]
section32 = condition32[condition32['Section'] == 1]

condition33 = parcels_data[(parcels_data['Township'] == 24) & (parcels_data['Range'] == 30)]
section33 = condition33[condition33['Section'].isin([2, 6])]

condition34 = parcels_data[(parcels_data['Township'] == 24) & (parcels_data['Range'] == 31)]
section34 = condition34[condition34['Section'].isin([17, 18, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30, 31, 32, 33, 34])]


#########25
condition35 = parcels_data[(parcels_data['Township'] == 25) & (parcels_data['Range'] == 29)]
section35 = condition35[condition35['Section'] == 3]

condition36 = parcels_data[(parcels_data['Township'] == 25) & (parcels_data['Range'] == 30)]
section36 = condition36[condition36['Section'].isin([4, 5, 6, 7, 8, 9, 10, 14, 17, 18, 19, 20, 21, 22, 27, 28, 29, 30, 31, 33, 34, 35])]

condition37 = parcels_data[(parcels_data['Township'] == 25) & (parcels_data['Range'] == 31)]
section37 = condition37[condition37['Section'] == 34]

condition38 = parcels_data[(parcels_data['Township'] == 25) & (parcels_data['Range'] == 32)]
section38 = condition38[condition38['Section'] == 2]

condition39 = parcels_data[(parcels_data['Township'] == 25) & (parcels_data['Range'] == 35)]
section39 = condition39[condition39['Section'].isin([8, 9, 10, 15, 17, 22])]


#########26
condition40 = parcels_data[(parcels_data['Township'] == 26) & (parcels_data['Range'] == 29)]
section40 = condition40[condition40['Section'].isin([13, 24, 25, 34])]

condition41 = parcels_data[(parcels_data['Township'] == 26) & (parcels_data['Range'] == 30)]
section41 = condition41[condition41['Section'].isin([30, 31, 32])]

condition42 = parcels_data[(parcels_data['Township'] == 26) & (parcels_data['Range'] == 31)]
section42 = condition42[condition42['Section'].isin([2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 22, 23])]

condition43 = parcels_data[(parcels_data['Township'] == 26) & (parcels_data['Range'] == 32)]
section43 = condition43[condition43['Section'].isin([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 17, 18])]

condition44 = parcels_data[(parcels_data['Township'] == 26) & (parcels_data['Range'] == 35)]
section44 = condition44[condition44['Section'] == 16]



#########27
condition45 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 30)]
section45 = condition45[condition45['Section'] == 24]

condition46 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 31)]
section46 = condition46[condition46['Section'].isin([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 34, 35])]

condition47 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 32)]
section47 = condition47[condition47['Section'].isin([3, 4, 5, 6, 19, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35])]

condition48 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 33)]
section48 = condition48[condition48['Section'].isin([1, 2, 5])]

condition49 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 34)]
section49 = condition49[condition49['Section'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13])]

condition50 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 35)]
section50 = condition50[condition50['Section'].isin([6, 7])]

condition51 = parcels_data[(parcels_data['Township'] == 27) & (parcels_data['Range'] == 36)]
section51 = condition51[condition51['Section'] == 27]


#########28
condition52 = parcels_data[(parcels_data['Township'] == 28) & (parcels_data['Range'] == 31)]
section52 = condition52[condition52['Section'].isin([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34])]

condition53 = parcels_data[(parcels_data['Township'] == 28) & (parcels_data['Range'] == 32)]
section53 = condition53[condition53['Section'].isin([[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]])]

condition54 = parcels_data[(parcels_data['Township'] == 28) & (parcels_data['Range'] == 33)]
section54 = condition54[condition54['Section'].isin([6, 13, 14, 15, 19, 20, 21, 23, 24, 25, 26, 27, 28, 32, 33, 34, 35])]

condition55 = parcels_data[(parcels_data['Township'] == 28) & (parcels_data['Range'] == 34)]
section55 = condition55[condition55['Section'].isin([1, 10, 11, 12, 19, 20, 21, 22, 25, 27, 28, 30, 31, 33, 34, 35, 36])]

condition56 = parcels_data[(parcels_data['Township'] == 28) & (parcels_data['Range'] == 35)]
section56 = condition56[condition56['Section'].isin([5, 6, 7, 31])]


#########29
condition57 = parcels_data[(parcels_data['Township'] == 29) & (parcels_data['Range'] == 29)]
section57 = condition57[condition57['Section'].isin([1, 2, 3, 11, 12, 13, 14, 15])]

condition58 = parcels_data[(parcels_data['Township'] == 29) & (parcels_data['Range'] == 30)]
section58 = condition58[condition58['Section'].isin([5, 6, 8, 20, 33])]

condition59 = parcels_data[(parcels_data['Township'] == 29) & (parcels_data['Range'] == 31)]
section59 = condition59[condition59['Section'].isin([32, 33, 34])]

condition60 = parcels_data[(parcels_data['Township'] == 29) & (parcels_data['Range'] == 32)]
section60 = condition60[condition60['Section'].isin([28, 29, 30, 31, 33, 34, 35, 36])]

condition61 = parcels_data[(parcels_data['Township'] == 29) & (parcels_data['Range'] == 34)]
section61 = condition61[condition61['Section'].isin([3, 4, 8, 9, 10, 13, 14, 15, 17, 18, 20, 21, 22, 23, 24, 26, 27, 28, 34, 35, 36])]

condition62 = parcels_data[(parcels_data['Township'] == 29) & (parcels_data['Range'] == 35)]
section62 = condition62[condition62['Section'].isin([17, 18, 19, 20, 21, 26, 27, 28, 29, 30, 31, 32, 33, 34])]


#########30
condition63 = parcels_data[(parcels_data['Township'] == 30) & (parcels_data['Range'] == 30)]
section63 = condition63[condition63['Section'].isin([28, 29, 30, 32, 33, 34, 35])]

condition64 = parcels_data[(parcels_data['Township'] == 30) & (parcels_data['Range'] == 31)]
section64 = condition64[condition64['Section'].isin([1, 2, 3, 10, 11, 12, 13, 14, 15, 21, 22])]

condition65 = parcels_data[(parcels_data['Township'] == 30) & (parcels_data['Range'] == 32)]
section65 = condition65[condition65['Section'].isin([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18])]

condition66 = parcels_data[(parcels_data['Township'] == 30) & (parcels_data['Range'] == 33)]
section66 = condition66[condition66['Section'].isin([4, 5, 6, 18, 22])]


#########31
condition67 = parcels_data[(parcels_data['Township'] == 31) & (parcels_data['Range'] == 29)]
section67 = condition67[condition67['Section'].isin([1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 17, 20, 21, 22, 24, 28])]

condition68 = parcels_data[(parcels_data['Township'] == 31) & (parcels_data['Range'] == 30)]
section68 = condition68[condition68['Section'].isin([3, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 28])]

condition69 = parcels_data[(parcels_data['Township'] == 31) & (parcels_data['Range'] == 31)]
section69 = condition69[condition69['Section'].isin([1, 2, 3, 10, 11, 12, 13, 14, 15, 22, 23, 24, 25, 26, 27, 34, 35])]

condition70 = parcels_data[(parcels_data['Township'] == 31) & (parcels_data['Range'] == 32)]
section70 = condition70[condition70['Section'].isin([3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])]

condition71 = parcels_data[(parcels_data['Township'] == 31) & (parcels_data['Range'] == 33)]
section71 = condition71[condition71['Section'].isin([28, 29, 30, 31, 32, 33])]

condition72 = parcels_data[(parcels_data['Township'] == 31) & (parcels_data['Range'] == 39)]
section72 = condition72[condition72['Section'] == 8]


#########32
condition73 = parcels_data[(parcels_data['Township'] == 32) & (parcels_data['Range'] == 29)]
section73 = condition73[condition73['Section'].isin([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33, 34, 35])]

condition74 = parcels_data[(parcels_data['Township'] == 32) & (parcels_data['Range'] == 30)]
section74 = condition74[condition74['Section'].isin([19, 20, 21, 22, 27, 28, 29, 30, 31])]

condition75 = parcels_data[(parcels_data['Township'] == 32) & (parcels_data['Range'] == 31)]
section75 = condition75[condition75['Section'].isin([23, 24, 25, 26, 27, 34, 35])]

condition76 = parcels_data[(parcels_data['Township'] == 32) & (parcels_data['Range'] == 32)]
section76 = condition76[condition76['Section'].isin([19, 20, 29, 30, 31, 32, 33])]


#########26
condition77 = parcels_data[(parcels_data['Township'] == 26) & (parcels_data['Range'] == 33)]
section77 = condition77[condition77['Section'].isin([7, 8, 9, 17, 18, 19, 20, 21, 28, 29, 30])]









appended_gdf = gpd.GeoDataFrame()

gdf_list = [section1, section2, section3, section4, section5, section6, section7, section8, section9, section10, section11, section12, section13, section14, section15,
            section16, section17, section18, section19, section20, section21, section22, section23, section24, section25, section26, section27, section28, section29,
            section30, section31, section32, section33, section34, section35, section36, section37, section38, section39, section40, section41, section42, section43,
            section44, section45, section46, section47, section48, section49, section50, section51, section52, section53, section54, section55, section56, section57,
            section58, section59, section60, section61, section62, section63, section64, section65, section66, section67, section68, section69, section70, section71,
            section72, section73, section74, section75, section76, section77]


for gdf in gdf_list:
    appended_gdf = appended_gdf.append(gdf, ignore_index=True)
#
# # unique_gdf = appended_gdf.drop_duplicates(subset=['Township', 'Range', 'Section', 'geometry'])
#
# appended_gdf.to_file(r'Nextera.shp')
#
# # dubs_test = gpd.read_file(r'Clearway3.shp')
duplicates = appended_gdf.duplicated(subset=['Township', 'Range', 'Section', 'geometry'])

print(len(duplicates[duplicates]))