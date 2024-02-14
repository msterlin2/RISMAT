import numpy as np
import matplotlib.pyplot as plt

def get_RP_2014_Male():
    # gets a vector of mortality rates for all male healthy annuitants ages 50-120 from the RP-2014 table
    mat = [0.004064, 0.004384, 0.004709, 0.005042, 0.005384,
           0.005735, 0.006099, 0.006478, 0.006877, 0.007305,
           0.007771, 0.008284, 0.008854, 0.009492, 0.010209,
           0.011013, 0.011916, 0.012930, 0.014067, 0.015342,
           0.016769, 0.018363, 0.020141, 0.022127, 0.024345,
           0.026826, 0.029608, 0.032735, 0.036258, 0.040232,
           0.044722, 0.049795, 0.055526, 0.061996, 0.069290,
           0.077497, 0.086712, 0.097038, 0.108591, 0.121499,
           0.135908, 0.151322, 0.167422, 0.184030, 0.201074,
           0.218559, 0.236535, 0.255059, 0.274170, 0.293848,
           0.313988, 0.334365, 0.354599, 0.374524, 0.393982,
           0.412831, 0.430946, 0.448227, 0.464592, 0.479987,
           0.494376, 0.5, 0.5, 0.5, 0.5,
           0.5, 0.5, 0.5, 0.5, 0.5,
           1.0]
    return mat

def get_RP_2014_Female():
    # gets a vector of mortality rates for all female healthy annuitants ages 50-120 from the RP-2014 table
    mat = [0.002768, 0.002905, 0.003057, 0.003225, 0.003412,
           0.003622, 0.003858, 0.004128, 0.004436, 0.004789,
           0.005191, 0.005646, 0.006156, 0.006723, 0.007352,
           0.008048, 0.008821, 0.009679, 0.010633, 0.011692,
           0.012868, 0.014171, 0.015614, 0.017210, 0.018977,
           0.020938, 0.023118, 0.025554, 0.028288, 0.031366,
           0.034844, 0.038783, 0.043246, 0.048305, 0.054032,
           0.060504, 0.067801, 0.076012, 0.085230, 0.095563,
           0.107126, 0.119744, 0.133299, 0.147720, 0.162971,
           0.179034, 0.195903, 0.213565, 0.231991, 0.251123,
           0.270858, 0.291040, 0.311444, 0.331900, 0.352232,
           0.372273, 0.391860, 0.410849, 0.429112, 0.446544,
           0.463061, 0.478604, 0.493137, 0.5, 0.5,
           0.5, 0.5, 0.5, 0.5, 0.5,
           1.0]
    return mat

def get_MP_2014_Male():
    # gets a matrix of mortality improvement rates for all male healthy annuitants ages 50-120 for years 2015 through 2027 from the MP-2014 table
    mat = [0.0233,0.0221,0.0205,0.0188,0.017,0.0153,0.0138,0.0126,0.0116,0.0109,0.0104,0.0101,0.01,
0.0226,0.0216,0.0203,0.0188,0.0171,0.0154,0.0139,0.0127,0.0116,0.0109,0.0104,0.0101,0.01,
0.0217,0.021,0.02,0.0186,0.0171,0.0155,0.0141,0.0128,0.0117,0.0109,0.0104,0.0101,0.01,
0.0195,0.0192,0.0185,0.0175,0.0162,0.0149,0.0136,0.0125,0.0115,0.0108,0.0103,0.0101,0.01,
0.017,0.0171,0.0167,0.016,0.0151,0.0141,0.0131,0.0121,0.0113,0.0107,0.0103,0.0101,0.01,
0.0145,0.015,0.015,0.0146,0.014,0.0133,0.0125,0.0117,0.0111,0.0106,0.0102,0.01,0.01,
0.0121,0.013,0.0134,0.0134,0.0131,0.0126,0.012,0.0114,0.0109,0.0105,0.0102,0.01,0.01,
0.0103,0.0113,0.0121,0.0125,0.0124,0.0121,0.0117,0.0113,0.0108,0.0104,0.0102,0.01,0.01,
0.0091,0.0102,0.0111,0.0117,0.012,0.0118,0.0116,0.0112,0.0108,0.0104,0.0102,0.01,0.01,
0.0084,0.0096,0.0105,0.0112,0.0117,0.0118,0.0116,0.0112,0.0109,0.0105,0.0102,0.0101,0.01,
0.0082,0.0094,0.0103,0.011,0.0115,0.0117,0.0117,0.0113,0.011,0.0106,0.0103,0.0101,0.01,
0.0082,0.0093,0.0103,0.011,0.0115,0.0117,0.0117,0.0115,0.0111,0.0107,0.0103,0.0101,0.01,
0.0084,0.0094,0.0103,0.011,0.0115,0.0117,0.0117,0.0116,0.0112,0.0108,0.0104,0.0101,0.01,
0.0089,0.0095,0.0103,0.011,0.0115,0.0117,0.0117,0.0116,0.0113,0.0108,0.0104,0.0101,0.01,
0.0096,0.0098,0.0103,0.0109,0.0114,0.0116,0.0117,0.0115,0.0112,0.0108,0.0104,0.0101,0.01,
0.0105,0.0103,0.0104,0.0108,0.0112,0.0115,0.0116,0.0114,0.0112,0.0108,0.0104,0.0101,0.01,
0.0118,0.011,0.0107,0.0108,0.011,0.0113,0.0114,0.0113,0.0111,0.0108,0.0104,0.0101,0.01,
0.0132,0.012,0.0113,0.011,0.011,0.0111,0.0112,0.0112,0.011,0.0107,0.0104,0.0101,0.01,
0.0147,0.0132,0.0121,0.0114,0.0111,0.011,0.011,0.011,0.0109,0.0106,0.0104,0.0101,0.01,
0.0161,0.0145,0.0132,0.0121,0.0114,0.0111,0.011,0.0109,0.0108,0.0106,0.0103,0.0101,0.01,
0.0174,0.0158,0.0143,0.013,0.012,0.0114,0.011,0.0108,0.0107,0.0105,0.0103,0.0101,0.01,
0.0186,0.017,0.0154,0.014,0.0127,0.0118,0.0112,0.0109,0.0106,0.0105,0.0103,0.0101,0.01,
0.0195,0.018,0.0164,0.0149,0.0135,0.0124,0.0116,0.011,0.0106,0.0104,0.0102,0.0101,0.01,
0.0202,0.0188,0.0172,0.0157,0.0143,0.013,0.012,0.0112,0.0107,0.0104,0.0102,0.0101,0.01,
0.0208,0.0194,0.0179,0.0164,0.015,0.0136,0.0125,0.0115,0.0109,0.0105,0.0102,0.0101,0.01,
0.0212,0.0198,0.0184,0.0169,0.0155,0.0141,0.0129,0.0119,0.0111,0.0106,0.0102,0.0101,0.01,
0.0215,0.0201,0.0187,0.0173,0.0159,0.0145,0.0133,0.0122,0.0113,0.0107,0.0103,0.0101,0.01,
0.0217,0.0203,0.0189,0.0175,0.0161,0.0148,0.0135,0.0124,0.0115,0.0108,0.0103,0.0101,0.01,
0.0219,0.0204,0.019,0.0176,0.0162,0.015,0.0137,0.0126,0.0116,0.0109,0.0104,0.0101,0.01,
0.022,0.0205,0.0191,0.0176,0.0163,0.015,0.0138,0.0127,0.0117,0.011,0.0104,0.0101,0.01,
0.022,0.0206,0.0191,0.0177,0.0163,0.015,0.0138,0.0128,0.0118,0.011,0.0104,0.0101,0.01,
0.022,0.0206,0.0191,0.0177,0.0163,0.015,0.0138,0.0127,0.0118,0.0111,0.0105,0.0101,0.01,
0.022,0.0206,0.0191,0.0177,0.0163,0.0149,0.0137,0.0127,0.0118,0.0111,0.0105,0.0101,0.01,
0.0219,0.0206,0.0191,0.0177,0.0163,0.0149,0.0137,0.0126,0.0117,0.011,0.0105,0.0101,0.01,
0.0217,0.0205,0.0191,0.0177,0.0163,0.0149,0.0137,0.0126,0.0117,0.0109,0.0104,0.0101,0.01,
0.0215,0.0203,0.0191,0.0177,0.0163,0.0149,0.0137,0.0126,0.0116,0.0109,0.0104,0.0101,0.01,
0.0213,0.0201,0.0189,0.0176,0.0162,0.0149,0.0136,0.0125,0.0115,0.0108,0.0102,0.0099,0.0099,
0.021,0.0199,0.0187,0.0174,0.0161,0.0148,0.0135,0.0124,0.0114,0.0106,0.0101,0.0098,0.0097,
0.0207,0.0196,0.0184,0.0172,0.016,0.0147,0.0135,0.0123,0.0113,0.0105,0.0099,0.0096,0.0096,
0.0203,0.0193,0.0182,0.017,0.0157,0.0145,0.0134,0.0122,0.0112,0.0104,0.0098,0.0095,0.0094,
0.02,0.019,0.0178,0.0167,0.0154,0.0142,0.0131,0.0121,0.0111,0.0103,0.0097,0.0093,0.0093,
0.0195,0.0185,0.0175,0.0163,0.0151,0.0139,0.0128,0.0118,0.0109,0.0101,0.0095,0.0092,0.0091,
0.019,0.0181,0.017,0.0159,0.0147,0.0136,0.0125,0.0115,0.0106,0.01,0.0094,0.009,0.009,
0.0183,0.0175,0.0165,0.0154,0.0143,0.0132,0.0121,0.0112,0.0103,0.0097,0.0092,0.0089,0.0088,
0.0176,0.0168,0.0159,0.0149,0.0138,0.0128,0.0118,0.0108,0.01,0.0094,0.0089,0.0087,0.0087,
0.0168,0.0161,0.0152,0.0143,0.0133,0.0123,0.0113,0.0104,0.0097,0.009,0.0086,0.0084,0.0085,
0.0159,0.0153,0.0145,0.0136,0.0126,0.0117,0.0108,0.0099,0.0092,0.0086,0.0082,0.008,0.0081,
0.0151,0.0145,0.0137,0.0129,0.012,0.0111,0.0102,0.0094,0.0087,0.0081,0.0078,0.0076,0.0077,
0.0143,0.0137,0.013,0.0122,0.0113,0.0104,0.0096,0.0089,0.0082,0.0077,0.0073,0.0072,0.0072,
0.0134,0.0129,0.0122,0.0114,0.0106,0.0098,0.0091,0.0083,0.0077,0.0072,0.0069,0.0067,0.0068,
0.0126,0.0121,0.0114,0.0107,0.01,0.0092,0.0085,0.0078,0.0072,0.0068,0.0065,0.0063,0.0064,
0.0118,0.0113,0.0107,0.01,0.0093,0.0086,0.0079,0.0073,0.0068,0.0063,0.006,0.0059,0.006,
0.0109,0.0105,0.0099,0.0093,0.0086,0.008,0.0074,0.0068,0.0063,0.0059,0.0056,0.0055,0.0055,
0.0101,0.0097,0.0092,0.0086,0.008,0.0074,0.0068,0.0063,0.0058,0.0054,0.0052,0.0051,0.0051,
0.0092,0.0089,0.0084,0.0079,0.0073,0.0068,0.0062,0.0057,0.0053,0.005,0.0047,0.0046,0.0047,
0.0084,0.008,0.0076,0.0072,0.0067,0.0061,0.0057,0.0052,0.0048,0.0045,0.0043,0.0042,0.0043,
0.0076,0.0072,0.0069,0.0064,0.006,0.0055,0.0051,0.0047,0.0043,0.0041,0.0039,0.0038,0.0038,
0.0067,0.0064,0.0061,0.0057,0.0053,0.0049,0.0045,0.0042,0.0039,0.0036,0.0035,0.0034,0.0034,
0.0059,0.0056,0.0053,0.005,0.0047,0.0043,0.004,0.0037,0.0034,0.0032,0.003,0.003,0.003,
0.005,0.0048,0.0046,0.0043,0.004,0.0037,0.0034,0.0031,0.0029,0.0027,0.0026,0.0025,0.0026,
0.0042,0.004,0.0038,0.0036,0.0033,0.0031,0.0028,0.0026,0.0024,0.0023,0.0022,0.0021,0.0021,
0.0034,0.0032,0.0031,0.0029,0.0027,0.0025,0.0023,0.0021,0.0019,0.0018,0.0017,0.0017,0.0017,
0.0025,0.0024,0.0023,0.0021,0.002,0.0018,0.0017,0.0016,0.0015,0.0014,0.0013,0.0013,0.0013,
0.0017,0.0016,0.0015,0.0014,0.0013,0.0012,0.0011,0.001,0.001,0.0009,0.0009,0.0008,0.0009,
0.0008,0.0008,0.0008,0.0007,0.0007,0.0006,0.0006,0.0005,0.0005,0.0005,0.0004,0.0004,0.0004,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0]
    mat = np.reshape(mat,(71,13))
    return mat

def get_MP_2014_Female():
    # gets a matrix of mortality improvement rates for all female healthy annuitants ages 50-120 for years 2015 through 2027 from the MP-2014 table
    mat = [0.0133,0.014,0.0142,0.014,0.0134,0.0126,0.0118,0.0111,0.0105,0.0101,0.01,0.01,0.01,
0.0111,0.0122,0.0128,0.013,0.0128,0.0123,0.0116,0.011,0.0105,0.0102,0.01,0.01,0.01,
0.0092,0.0105,0.0114,0.0119,0.0121,0.0119,0.0115,0.0109,0.0105,0.0102,0.01,0.01,0.01,
0.0077,0.0091,0.0102,0.011,0.0114,0.0115,0.0113,0.011,0.0106,0.0103,0.0101,0.01,0.01,
0.0066,0.008,0.0093,0.0103,0.0109,0.0112,0.0111,0.0109,0.0106,0.0103,0.0101,0.01,0.01,
0.0061,0.0074,0.0087,0.0097,0.0105,0.0109,0.011,0.0109,0.0107,0.0104,0.0102,0.01,0.01,
0.0061,0.0072,0.0084,0.0094,0.0102,0.0108,0.011,0.011,0.0108,0.0105,0.0102,0.0101,0.01,
0.0068,0.0075,0.0084,0.0094,0.0101,0.0107,0.011,0.011,0.0108,0.0106,0.0103,0.0101,0.01,
0.008,0.0083,0.0088,0.0095,0.0102,0.0107,0.011,0.0111,0.0109,0.0106,0.0103,0.0101,0.01,
0.0095,0.0094,0.0095,0.0099,0.0104,0.0108,0.011,0.0111,0.011,0.0107,0.0104,0.0101,0.01,
0.0113,0.0107,0.0105,0.0105,0.0107,0.0109,0.0111,0.0111,0.011,0.0107,0.0104,0.0101,0.01,
0.0132,0.0122,0.0115,0.0112,0.011,0.0111,0.0111,0.0111,0.0109,0.0107,0.0104,0.0101,0.01,
0.0149,0.0137,0.0127,0.0119,0.0115,0.0113,0.0111,0.011,0.0109,0.0106,0.0104,0.0101,0.01,
0.0164,0.015,0.0138,0.0128,0.012,0.0115,0.0112,0.011,0.0108,0.0106,0.0103,0.0101,0.01,
0.0177,0.0162,0.0148,0.0136,0.0126,0.0118,0.0113,0.011,0.0108,0.0105,0.0103,0.0101,0.01,
0.0188,0.0172,0.0157,0.0143,0.0132,0.0122,0.0115,0.0111,0.0107,0.0105,0.0103,0.0101,0.01,
0.0197,0.0181,0.0165,0.015,0.0137,0.0126,0.0118,0.0112,0.0107,0.0104,0.0102,0.0101,0.01,
0.0204,0.0188,0.0172,0.0157,0.0143,0.0131,0.0121,0.0114,0.0108,0.0105,0.0102,0.0101,0.01,
0.021,0.0195,0.0179,0.0163,0.0149,0.0136,0.0125,0.0116,0.0109,0.0105,0.0102,0.0101,0.01,
0.0214,0.02,0.0184,0.0169,0.0154,0.014,0.0128,0.0118,0.0111,0.0106,0.0102,0.0101,0.01,
0.0217,0.0204,0.0189,0.0173,0.0158,0.0144,0.0131,0.0121,0.0113,0.0107,0.0103,0.0101,0.01,
0.0218,0.0206,0.0192,0.0177,0.0162,0.0147,0.0134,0.0123,0.0114,0.0108,0.0103,0.0101,0.01,
0.0217,0.0206,0.0193,0.0179,0.0164,0.015,0.0137,0.0125,0.0116,0.0108,0.0104,0.0101,0.01,
0.0215,0.0205,0.0193,0.018,0.0166,0.0152,0.0139,0.0127,0.0117,0.0109,0.0104,0.0101,0.01,
0.0211,0.0202,0.0191,0.0179,0.0166,0.0153,0.014,0.0128,0.0118,0.011,0.0104,0.0101,0.01,
0.0208,0.0199,0.0189,0.0178,0.0166,0.0153,0.0141,0.0129,0.0119,0.0111,0.0105,0.0101,0.01,
0.0206,0.0197,0.0187,0.0176,0.0165,0.0153,0.0141,0.013,0.0119,0.0111,0.0105,0.0101,0.01,
0.0204,0.0195,0.0185,0.0174,0.0164,0.0152,0.0141,0.013,0.012,0.0111,0.0105,0.0101,0.01,
0.0203,0.0193,0.0183,0.0173,0.0162,0.0151,0.014,0.013,0.012,0.0112,0.0105,0.0101,0.01,
0.0203,0.0193,0.0183,0.0172,0.0161,0.015,0.014,0.013,0.012,0.0112,0.0105,0.0101,0.01,
0.0203,0.0194,0.0183,0.0172,0.0161,0.015,0.0139,0.013,0.012,0.0112,0.0106,0.0101,0.01,
0.0204,0.0195,0.0184,0.0173,0.0161,0.015,0.0139,0.0129,0.012,0.0112,0.0106,0.0102,0.01,
0.0206,0.0196,0.0185,0.0174,0.0162,0.015,0.0139,0.0129,0.012,0.0112,0.0106,0.0102,0.01,
0.0208,0.0198,0.0187,0.0175,0.0163,0.0151,0.0139,0.0129,0.0119,0.0112,0.0106,0.0102,0.01,
0.021,0.02,0.0189,0.0177,0.0164,0.0152,0.014,0.0129,0.0119,0.0111,0.0105,0.0102,0.01,
0.0213,0.0202,0.0191,0.0178,0.0165,0.0153,0.014,0.0129,0.0119,0.0111,0.0105,0.0101,0.01,
0.0215,0.0204,0.0192,0.0179,0.0166,0.0153,0.014,0.0128,0.0118,0.011,0.0103,0.0099,0.0099,
0.0217,0.0205,0.0192,0.0179,0.0166,0.0153,0.014,0.0128,0.0117,0.0108,0.0102,0.0098,0.0097,
0.0218,0.0205,0.0192,0.0178,0.0165,0.0152,0.0139,0.0127,0.0116,0.0107,0.01,0.0096,0.0096,
0.0217,0.0204,0.019,0.0176,0.0162,0.0149,0.0137,0.0125,0.0114,0.0105,0.0099,0.0095,0.0094,
0.0216,0.0203,0.0189,0.0174,0.016,0.0147,0.0134,0.0123,0.0113,0.0104,0.0097,0.0093,0.0093,
0.0214,0.0201,0.0187,0.0172,0.0158,0.0144,0.0131,0.012,0.0111,0.0102,0.0096,0.0092,0.0091,
0.0212,0.0199,0.0185,0.017,0.0156,0.0142,0.0129,0.0117,0.0108,0.0101,0.0094,0.009,0.009,
0.0208,0.0196,0.0182,0.0168,0.0153,0.0139,0.0126,0.0115,0.0105,0.0098,0.0093,0.0089,0.0088,
0.0204,0.0193,0.0179,0.0165,0.015,0.0136,0.0123,0.0112,0.0102,0.0095,0.009,0.0087,0.0087,
0.0199,0.0188,0.0176,0.0162,0.0147,0.0133,0.012,0.0109,0.0099,0.0092,0.0087,0.0084,0.0085,
0.0189,0.0179,0.0167,0.0154,0.014,0.0127,0.0114,0.0103,0.0094,0.0087,0.0082,0.008,0.0081,
0.0179,0.0169,0.0158,0.0146,0.0133,0.012,0.0108,0.0098,0.0089,0.0083,0.0078,0.0076,0.0077,
0.0169,0.016,0.0149,0.0137,0.0125,0.0113,0.0102,0.0092,0.0084,0.0078,0.0074,0.0072,0.0072,
0.0159,0.0151,0.014,0.0129,0.0118,0.0107,0.0096,0.0087,0.0079,0.0073,0.0069,0.0068,0.0068,
0.0149,0.0141,0.0132,0.0121,0.0111,0.01,0.009,0.0082,0.0074,0.0069,0.0065,0.0063,0.0064,
0.0139,0.0132,0.0123,0.0113,0.0103,0.0093,0.0084,0.0076,0.0069,0.0064,0.0061,0.0059,0.006,
0.0129,0.0122,0.0114,0.0105,0.0096,0.0087,0.0078,0.0071,0.0064,0.006,0.0056,0.0055,0.0055,
0.0119,0.0113,0.0105,0.0097,0.0088,0.008,0.0072,0.0065,0.0059,0.0055,0.0052,0.0051,0.0051,
0.0109,0.0104,0.0097,0.0089,0.0081,0.0073,0.0066,0.006,0.0055,0.005,0.0048,0.0046,0.0047,
0.0099,0.0094,0.0088,0.0081,0.0074,0.0067,0.006,0.0054,0.005,0.0046,0.0043,0.0042,0.0043,
0.0089,0.0085,0.0079,0.0073,0.0066,0.006,0.0054,0.0049,0.0045,0.0041,0.0039,0.0038,0.0038,
0.008,0.0075,0.007,0.0065,0.0059,0.0053,0.0048,0.0044,0.004,0.0037,0.0035,0.0034,0.0034,
0.007,0.0066,0.0061,0.0057,0.0052,0.0047,0.0042,0.0038,0.0035,0.0032,0.003,0.003,0.003,
0.006,0.0057,0.0053,0.0049,0.0044,0.004,0.0036,0.0033,0.003,0.0028,0.0026,0.0025,0.0026,
0.005,0.0047,0.0044,0.004,0.0037,0.0033,0.003,0.0027,0.0025,0.0023,0.0022,0.0021,0.0021,
0.004,0.0038,0.0035,0.0032,0.0029,0.0027,0.0024,0.0022,0.002,0.0018,0.0017,0.0017,0.0017,
0.003,0.0028,0.0026,0.0024,0.0022,0.002,0.0018,0.0016,0.0015,0.0014,0.0013,0.0013,0.0013,
0.002,0.0019,0.0018,0.0016,0.0015,0.0013,0.0012,0.0011,0.001,0.0009,0.0009,0.0008,0.0009,
0.001,0.0009,0.0009,0.0008,0.0007,0.0007,0.0006,0.0005,0.0005,0.0005,0.0004,0.0004,0.0004,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0]
    mat = np.reshape(mat,(71,13))
    return mat


def client_process(client):
    
    #MS - Ignoring initial screen settings and letting python handle it. 
    #MS - Code below is retained for consistency with the original Matlab code

    # make entire screen white
    #ss = (0, 0, 1280, 720)  # Example screen size, change as needed
    #figwhite = plt.figure()
    #figwhite.set_size_inches(ss[2] / 100, ss[3] / 100)
    #figwhite.patch.set_facecolor((1, 1, 1))

    # compute figure position and add to client
    #figsize = client.figureSize
    #if len(figsize) < 2:
        #ss = (0, 0, 1920, 1080)  # Example screen size, change as needed
    #    figsize = [.9 * ss[2], .9 * ss[3]]
    #figw = figsize[0]
    #figh = figsize[1]
    #ss = (0, 0, 1920, 1080)  # Example screen size, change as needed
    #x1 = (ss[2] - figw) / 2
    #x2 = (ss[3] - figh) / 2
    #client.figurePosition = [x1, x2, figw, figh]

    # ------------ get vectors of mortality rates for person 1
    # make vectors for rows and columns of mortality tables
    ages = np.arange(50, 121, 1).reshape(-1, 1)  # ages (rows in mortality tables)
    years = np.arange(2014, 2113)  # years (columns in mortality tables)

    # computing mortalities for person 1
    if client.p1Sex == 'M':
        m1 = get_RP_2014_Male()  # get mortalities for 2014
        m2 = get_MP_2014_Male()  # get mortality improvement rates 2015-2027
    else:
        m1 = get_RP_2014_Female()  # get mortalities for 2014
        m2 = get_MP_2014_Female()  # get mortality improvement rates 2015-2027

    m1 = np.array(m1) #MS - converts the list to a numpy array
    m1 = m1.reshape(-1,1) #MS - shapes the array into a column vector 

    # extend mortality improvement rates to 2113 using ultimate rates for 2027
    m2027 = m2[:,12] 
    m2027 = m2027.reshape(-1,1)
    m3 = m2027* np.ones((1,86))
    
    # make mortality table from 2014 through 2113
    m4 = np.concatenate((m1, 1 - m2, 1 - m3), axis=1) #join 2014 mortality and mortality factors (1 - improvement)
    mortTable = np.cumprod(m4, axis=1) # multiply 2014 mortality by cumulative factors
    
    # get vector of mortality rates for p1Age to age 120 beginning in client.year
    rowNumber = np.where(ages == client.p1Age)[0][0] # find row for p1 age
    colNumber = np.where(years == client.Year)[0][0] # find column for current year 
    m5 = mortTable[rowNumber:, colNumber:] #create new matrix
    mortP1 = np.diag(m5)

    # ------------ get vectors of mortality rates for person 2
    # make vectors for rows and columns of mortality tables
    ages = np.arange(50, 121, 1).reshape(-1, 1)  # ages (rows in mortality tables)
    years = np.arange(2014, 2113)  # years (columns in mortality tables)

    # compute mortalities for person 2
    if client.p2Sex == 'M':
        m1 = get_RP_2014_Male()  # get mortalities for 2014
        m2 = get_MP_2014_Male()  # get mortality improvement rates 2015-2027
    else:
        m1 = get_RP_2014_Female()  # get mortalities for 2014
        m2 = get_MP_2014_Female()  # get mortality improvement rates 2015-2027

    m1 = np.array(m1)
    m1 = m1.reshape(-1,1)

    # extend mortality improvement rates to 2113 using ultimate rates for 2027
    m2027 = m2[:,12] 
    m2027 = m2027.reshape(-1,1)
    m3 = m2027* np.ones((1,86))
    
    # make mortality table from 2014 through 2113
    m4 = np.concatenate((m1, 1 - m2, 1 - m3), axis=1) # join 2014 mortality and mortality factors (1 - improvement)
    mortTable = np.cumprod(m4, axis=1) # multiply 2014 mortality by cumulative factors
    
    # get vector of mortality rates for p2Age to age 120 beginning in client.year
    rowNumber = np.where(ages == client.p2Age)[0][0] # find row for p2 age
    colNumber = np.where(years == client.Year)[0][0] # find column for current year
    m5 = mortTable[rowNumber:, colNumber:] # create new matrix
    mortP2 = np.diag(m5)

    # ----- extend shorter of mortality vectors to length of longer
    ncols = max(len(mortP1), len(mortP2)) # number of columns in longer vector
    mortP1 = np.concatenate((mortP1, np.ones(ncols - len(mortP1))))
    mortP2 = np.concatenate((mortP2, np.ones(ncols - len(mortP2))))

    # ----- add zero mortality for year 1
    mortP1 = np.concatenate(([0], mortP1))
    mortP2 = np.concatenate(([0], mortP2))
    ncols += 1

    # add mortalities to the client data structure
    client.mortP1 = mortP1
    client.mortP2 = mortP2

    # make personal state matrix
    nrows = client.nScenarios  # Number of rows in scenario matrices

    # Person 1
    probs = np.ones((nrows, 1)) * mortP1  # Probabilities of dying for person 1
    randnums = np.random.rand(nrows, ncols)  # Random numbers
    statesP1 = (randnums >= probs).astype(float)  # 1 if alive, 0 if dead
    statesP1 = np.cumprod(statesP1, axis=1)  # Survival status, 1 if alive, 0 if dead

    # Person 2
    probs = np.ones((nrows, 1)) * mortP2  # Probabilities of dying for person 2
    randnums = np.random.rand(nrows, ncols)  # Random numbers
    statesP2 = (randnums >= probs).astype(float)  # 1 if alive, 0 if dead
    statesP2 = np.cumprod(statesP2, axis=1)  # Survival status, 1 if alive, 0 if dead
    statesP2 *= 2  # Code as 2 for person 2

    # Add person 1 and person 2
    states = statesP1 + statesP2

    # Add estate (4) whenever 0 is preceded by 1, 2, or 3
    estates = (states[:, 1:ncols] == 0) & (states[:, :ncols - 1] > 0)
    estates = np.concatenate((np.zeros((nrows, 1), dtype=float), estates), axis=1)
    states = states + 4 * estates

    # put in client scenario matrix
    client.pStatesM = states

    # Compute life expectancy for p1
    surv1 = np.cumprod(1 - mortP1)
    ncols = len(surv1)
    propdie = surv1[:ncols-1] - surv1[1:ncols]
    client.p1LE = np.sum(propdie * np.arange(1, len(propdie) + 1))
    client.p1LE = int(0.1 * round(client.p1LE * 10))

    # Compute life expectancy for p2
    surv2 = np.cumprod(1 - mortP2)
    ncols = len(surv2)
    propdie = surv2[:ncols-1] - surv2[1:ncols]
    client.p2LE = np.sum(propdie * np.arange(1, len(propdie) + 1))
    client.p2LE = int(0.1 * round(client.p2LE * 10))

    # create empty client incomes matrix
    client.incomesM = np.zeros_like(client.pStatesM)

    # create empty client fees matrix
    client.feesM = np.zeros_like(client.pStatesM)

    return client

