
# Dry Bean Linear Discriminant and Principal Component Analysis with Logistic Regression

## Problem Statement

The purpose of this study is based on the available data, it was predicted after analyzes whether class is Seker, Barbunya, Bombay, Cali, Dermosan, Horoz or Sira.

## Dataset

This breast cancer database was obtained from the **Faculty of Technology, Selcuk University, Turkey.** Dataset is downloaded from [archive.ics.uci.edu](https://archive.ics.uci.edu/ml/datasets/Dry+Bean+Dataset) website. You can find the details of the dataset in that website. Dataset has **17 columns** and **13612 rows with the header**. If you publish resultswhen using this database, then please include the link in your acknowledgements.

> Seven different types of dry beans were used in this research, taking
> into account the features such as form, shape, type, and structure by
> the market situation. A computer vision system was developed to
> distinguish seven different registered varieties of dry beans with
> similar features in order to obtain uniform seed classification. For
> the classification model, images of **13,611 grains** of **7 different
> registered dry beans** were taken with a high-resolution camera. Bean
> images obtained by computer vision system were subjected to
> segmentation and feature extraction stages, and a total of **16
> features; 12 dimensions and 4 shape forms**, were obtained from the
> grains. 

This explanation also included in [archive.ics.uci.edu](https://archive.ics.uci.edu/ml/datasets/Dry+Bean+Dataset) website.

## Methodology

In this project, as stated in the title, results were obtained through **Logistic Regression**, **Linear Discriminant Analysis** and **Principal Component Analysis** methods. 

## Analysis

| # | Column | Non-Null Count | Dtype |
|--|--|--|--|
| 0 | Area | 13611 non-null | int64
| 1 | Perimeter | 13611 non-null | float64
| 2 | MajorAxisLength | 13611 non-null | float64
| 3 | MinorAxisLength | 13611 non-null | float64
| 4 | AspectRation | 13611 non-null | float64
| 5 | Eccentricity | 13611 non-null |float64
| 6 | ConvexArea | 13611 non-null | int64
| 7 | EquivDiameter | 13611 non-null | float64
| 8 | Extent | 13611 non-null | float64
| 9 | Solidity | 13611 non-null | float64
| 10 | roundness | 13611 non-null | float64
| 11 | Compactness | 13611 non-null | float64
| 12 | ShapeFactor1 | 13611 non-null | float64
| 13 | ShapeFactor2 | 13611 non-null | float64
| 14 | ShapeFactor3 | 13611 non-null | float64
| 15 | ShapeFactor4 | 13611 non-null | float64
| 16 | Class | 13611 non-null | object

### **Number of Duplicated Values:**

> **Number of duplicated values:**   68  
 
**After removing duplicate rows based on all columns.** 
> **Number of duplicated values:**   0

### **Confusion Matrices and Accuracy Scores**

***Actual / Without PCA Confusion Matrix :***
| 227 | 0 | 16 | 0 | 1 | 3 | 10 |
|--|--|--|--|--|--|--|
| **0** | **95** | **0** | **0** | **0** | **0** | **0** |
| **7** | **0** | **320** | **0** | **6** | **1** | **5** |
| **0** | **0** | **0** | **685** | **1** | **14** | **42** |
| **3** | **0** | **6** | **5** | **348** | **0** | **11** |
| **1** | **0** | **0** | **1** | **0** | **359** | **14** |
| **1** | **0** | **0** | **50** | **9** | **12** | **456** |

> **Accuracy score: 0.9191583610188261**

***Actual / With PCA Confusion Matrix :***
| 169 | 0 | 64 | 0 | 2 | 2 | 20 |
|--|--|--|--|--|--|--|
| **0** | **95** | **0** | **0** | **0** | **0** | **0** |
| **62** | **0** | **266** | **0** | **4** | **1** | **6** |
| **0** | **0** | **0** | **685** | **1** | **14** | **42** |
| **0** | **0** | **13** | **4** | **346** | **0** | **10** |
| **1** | **0** | **0** | **2** | **0** | **357** | **15** |
| **0** | **0** | **0** | **53** | **14** | **13** | **448** |

> **Accuracy score: 0.8733850129198967**

***Without PCA and with PCA Confusion Matrix :***
| 164 | 0 | 59 | 0 | 2 | 0 | 14 |
|--|--|--|--|--|--|--|
| **0** | **95** | **0** | **0** | **0** | **0** | **0** |
| **65** | **0** | **277** | **0** | **0** | **0** | **0** |
| **0** | **0** | **0** | **732** | **2** | **3** | **4** |
| **0** | **0** | **6** | **1** | **354** | **0** | **4** |
| **0** | **0** | **0** | **3** | **0** | **378** | **8** |
| **3** | **0** | **1** | **8** | **9** | **6** | **511** |

> **Accuracy score: 0.9269102990033222**

***LDA and Actual Confusion Matrix :***
| 184 | 0 | 37 | 0 | 3 | 0 | 15 |
|--|--|--|--|--|--|--|
| **0** | **95** | **0** | **0** | **0** | **0** | **0** |
| **36** | **0** | **306** | **0** | **0** | **0** | **0** |
| **2** | **0** | **0** | **591** | **0** | **113** | **35** |
| **0** | **0** | **4** | **0** | **359** | **0** | **2** |
| **2** | **0** | **0** | **242** | **0** | **130** | **15** |
| **3** | **0** | **1** | **59** | **6** | **0** | **469** |

> **Accuracy score: 0.7877445551864156**

**Process took 3.976813316345215 seconds.**

## How to Run Code

Before running the code make sure that you have these libraries:

 - pandas 
 - time
 - sklearn
 - warnings
    
## Contact Me

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak).  
 - Mail address: doguilmak@gmail.com
 