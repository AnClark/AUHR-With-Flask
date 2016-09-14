/**
 * 日期处理函数
 * 用于将标准的 UTC 时间日期格式转换成我们熟悉的标准“yy/mm/dd”格式。
 * 也就是说，从以下格式——
 *      Wed, 14 Sep 2016 15:02:06 GMT
 * 转换为
 *      2016/09/14
 *
 * ●为什么要写这个函数？
 *      因为我的工程中要使用表单控件 date。它只能识别标准格式！
 *
 * ●输入参数
 *      date_object：一个 Date 对象。SQLAlchemy 的日期字段查询结果在JavaScript中表现出来的也是这个格式。
 * ●输出结果
 *      一个标准日期字符串（yy/mm/dd）。
 *
 * Created by AnCla on 2016/9/14 0014.
 */


function UTC2StandardFormat(date_object){

    //将可能传递过来的时间字符串重新整合生成日期对象
    var date = new Date(date_object);
    //获取年月日
        var year = date.getFullYear();
        var month = date.getMonth()+1;  /** 注意：getMonth() 的返回值范围是 0至11  **/
        var day = date.getDate();
    //定义年月日字符串，以便拼接
        var str_year = String(year);
        var str_month = String(month);
        var str_day = String(day);
    //手动格式化
        //若年/月/日小于千位/十位数，则自动补零
    if(year<1000){
        str_year = '0' + str_year;
    }
    if(month<10){
        str_month = '0' + str_month;
    }
    if(day<10){
        str_day = '0' + str_day;
    }

    return String(str_year + '-' + str_month + '-' + str_day)
}