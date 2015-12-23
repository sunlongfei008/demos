#ifndef SMS_ICE
#define SMS_ICE

module SMS {
    ["python:seq:list"] sequence <string> PhoneSeq;

    dictionary <string, string> SmsDict;

    interface SmsSend {

        //实时发送短信，phones是单个或多个电话号码，多个电话号码以逗号
        //分割，tempId为短信模板，可以通过getSmsTemplates获取所有模板。
        SmsDict sendStandard(string phones, string tempId);

        //定时发送短信，phones和tempId同上，date为定时发送的时间，格式为
        //"yyyy-MM-dd HH:mm:ss"
        SmsDict sendScheduler(string phones, string tempId, string date);

        //发送验证码，phone为单个电话号码，temId同上
        SmsDict sendIdentifyingCode(string phone, string tempId);

        //查看验证码是否有效，phone同上，code为验证码
        SmsDict checkIdentifyingCode(string phone, string code);

        //获取短信模板信息
        SmsDict getSmsTemplates();

        SmsDict test();
    };
};

#endif
