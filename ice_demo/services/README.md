#ICE服务端

##运行
$ python server.py

##接口文件

接口文件存放在interface目录下，以*.ice命名，服务端自动加载interface目录中的接口文件

##接口库文件
接口库文件是用python编写的库文件，在libs/api/目录下，以"I.py"结尾的文件，库文件需要到
config目录中的setting.py文件的INSTALLED_SERVANTS参数注册，才能加载

