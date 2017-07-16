# scikit-learn
scikit-learn-master/：scikit-learn源代码<br>
scikit-learn-script/：<br>
>iris.txt:原始数据<br>
>dataset:对原始数据shuffle后的数据<br>
>train/：训练集<br>
>test/：测试集<br>
>loadData.py：加载数据方法测试，使用numpy的loadtxt方法直接加载文件生成对应的矩阵<br>
>shuffleFile.py：对原始数据进行shuffle<br>
>splitFileScript.py：根据自定义比率(ratio)将数据文件切分为训练集与测试集,同时将内容与标签分离，放入x文件与y文件<br>
>dataProcess.py：数据处理脚本，用于加载数据、计算准确率及配置参数<br>
>LogisticRegressionTest.py：逻辑回归<br>
>NaiveBayesTest.py：朴素贝叶斯分类器<br>
>KNNTest.py：最近邻分类器<br>
>DecissionTreeTest.py：决策树分类器<br>
>SVMTest.py：支持向量机分类器<br>