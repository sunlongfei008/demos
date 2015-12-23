<?php
require 'Ice.php';
require 'sms.php';

$ic = null;
try
{
     $ic = Ice_initialize();                 //初始化ice的客户端
     $base = $ic->stringToProxy("sms:default -h localhost -p 10000");//创建代理参数
     $proxy = SMS_SmsSendPrxHelper::checkedCast($base);//建立代理链接
     if(!$proxy)
          throw new RuntimeException("Invalid proxy");
     //调用接口,这是一个测试接口
     $result = $proxy->test();
     print_r($result);

     //以下的所有接口都是我们的服务提供的接口
     // $phones:单个或多个电话号码字符串，多个电话号码以逗号分割
     // $phone:单个电话号码
     // $tempId:短信模板ID，可以通过getSmsTemplates()获取所有的短信模板
     // $date:发送时间，格式为"yyyy-MM-dd HH:mm:ss"
     // $code:短信验证码
     // $result = $proxy->sendStandard($phones, $tempId);
     // $result = $proxy->sendScheduler($phones, $message, $date);
     // $result = $proxy->sendIdentifyingCode($phone, $tempId);
     // $result = $proxy->checkIdentifyingCode($phone, $code);
     // $result = $proxy->getSmsTemplates();
     // print_r($result);
}
catch(Exception $ex)
{
     echo $ex;
}

if($ic)
{
// Clean up
try
{
     $ic->destroy();
}
catch(Exception $ex)
{
     echo $ex;
}
}
?>
