# miaosha

**简介**
miaoshi 是基于京东&天猫的商品秒杀工具。
用户可以根据实际情况设置定期任务，也可以根据需要设置单一任务。


**截止2023年9月中旬项目未完成工作进度计划**

```plantuml
@startgantt
projectscale weekly zoom 3
saturday are closed
sunday are closed

Project starts 2023-09-15

[京东登录与下单模拟业务层] as [jd_service] starts 2023-09-15 and lasts 1 weeks
[天猫登录与下单模拟业务层] as [tm_service] starts 2023-09-15 and lasts 1 weeks

[页面交互UI] as [UI] lasts 3 weeks and starts at [jd_service]'s end

[Test] as [T] lasts 1 week and starts at [UI]'s end

@endgantt
```