Assignment1
==
# 1、摘要
本项目的目标是基于LSTM这一深度学习模型，对标的物价格进行预测。
# 2、参考资料
1、《基于LSTM的比特币价格预测模型（系列1）》
2、《预测股市崩盘基于统计机器学习与神经网络》
3、《严谨解决5种机器学习算法在预测股价的应用》
# 3、研究过程
## 1、数据获取
根据参考资料1中的要求，我通过币安交易所的API获取资料中所述的三种交易对的价格数据，具体代码可见data_get文件。在编写该代码过程中发现币安API文档中Base_url（https://api.binance.com） 无法链接，经过查阅资料，将Base_url改为（https://api.binancezh.cc ）成功解决了链接问题。
## 2、创建并调整LSTM模型
由于无法找到资料1中的 ccrypto library所以我们采用了资料2中所述的tensorflow来构建所需的LSTM模型，本项目所使用的library版本为tensorflow==1.9.0，keras==2.2.0。
随后，主要根据资料3中的研究使用Vanguard Total Stock Market ETF（VTI）的每日调整收盘价作为研究标的物，使用VTI从2015年11月25日至2018年11月23日三年的历史价格，将数据集分为60%训练集、20%验证集和20%测试集。使用训练集对模型进行训练，使用验证集对模型超参数进行调整，最后使用测试集对模型的性能进行测试。
### (1)使用前60%的数据训练LSTM，得到如下基本模型
![](Screen_shot/model_summary.PNG)
### (2)确定最佳参数N
![](Screen_shot/optimal_N.PNG)

我们可以得到在N=3时，RMSE最小，所以N_optimal=3
### (3)确定最佳参数epochs and batch_size
![](Screen_shot/opt_batch_epochs.PNG)

optimum epochs = 50
optimum batch_size = 8
这时RMSE最小
### (4)确定最佳参数LSTM units and dropout prob
![](Screen_shot/opt_units_dropprob.PNG)

optimum lstm_units = 128
optimum dropout_prob = 1.0
这时RMSE最小
### (5)确定最佳optimizer
最佳optimizer是nadam，RMSE最小

## 3、最终LSTM模型及test结果
N=3,epochs=50,batch_size=8,lstm_units=128,dropput_prob=1.0,optimizer='nadam'
![](Screen_shot/final_result.png)

RMSE on test set = 1.164
MAPE on test set = 0.583%



