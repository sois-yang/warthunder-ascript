# -*- coding: utf-8 -*-
###脚本——战雷海战
###作者：t--yang
###说明：本脚本为战雷海战自动战斗脚本，使用airscript框架编写。
###使用说明：请先安装airscript框架，然后运行本脚本即可开始自动战斗。
###注意事项：本脚本仅供学习交流使用，请勿用于非法用途。
###版权所有，侵权必究。
###联系作者：t--yang-only@outlook.com
###版本：1.0
###日期：2024-07-23  构建基本逻辑
###更新日志：1.1
###更新内容：2024-08-04 重构代码,加入超时重启
###更新日志：1.2
###更新内容：2024-08-07 再次重构,加入用户邮箱反馈,加入时间计时
###更新日志：1.3
###更新内容：2024-08-08 重构,加入邮箱控制
###更新日志：1.4
###更新内容：2024-08-09 简单修复bug,加入简易自动战斗
###更新日志：1.5
###更新内容：2024-08-10 重构战斗部分
###更新日志：1.6
###更新内容：2024-08-17 重构重启,用户控制,邮件反馈,优化时长计算
###更新日志：1.7
###更新内容：2024-08-24 重构战斗部分,用户控制,邮件反馈,优化时长计算
###更新日志：1.8
###更新内容：2024-08-25 修复所有已知,高几率bug,完结收工,陆战beta/空战beta心情好再写打包睡觉
###更新日志：1.9
###更新内容：2024-08-30 修复bug,加入加速器切换节点,陆战自动
###更新日志：2.0
###更新内容：2024-09-08 修复时长计算
###更新日志：2.1
###更新内容：2024-09-15 修复bug,加入Yolo识别,优化脚本流程,空战自动(基本不能用),增加多种加速器自动切换
###更新日志：2.2
###更新内容：2024-09-21 修复bug,优化脚本流程,优化了更新与游戏崩溃的处理方法,解决一些偶然bug
###更新日志：2.3
###更新内容：2024-10-1 修复bug,优化脚本流程,空战弱ai,模仿真人进行三模式随机游戏,优化时长与邮件控制
###更新日志：2.4
###更新内容：2024-10-3 修复bug,优化脚本流程,改进游戏思路
###更新日志：2.5
###更新内容：2024-10-3 精简流程,在线提交代码,对最新的游戏更新做出针对性优化
###更新日志：2.6
###更新内容：2024-10-5 重写流程,增加多重用户操作修正,小时bug率降至13.74%
###更新日志：2.7
###更新内容：2024-10-20 修复bug,优化反馈
###更新日志：2.8
###更新内容：2024-11-3 修复bug,优化流程,ai大更，针对游戏新版本进行优化
###更新日志：2.9
###更新内容：2024-11-17 优化极限模式，优化更新
###更新日志：3.0
###更新内容：2024-11-23 针对官方的界面改动进行优化,对于官方的制裁
版本 = 3.0
时长 = 100
时长小时0 = 0
时长分钟0 = 0
用户邮箱 = "xxxx@xxxx.com"
报告邮箱 = "xxxx@xxxx.com"

模式=2 #1打包版 #2脚本版
if "必须参数":
    发送邮箱1 = "xxx@163.com"  # 仅163邮箱
    发送邮箱2 = "xxx@163.com"
    发送邮箱3 = "xxx@163.com"
    发送邮箱4 = "xxx@163.com"
    发送邮箱5 = "xxx@163.com"
    发送邮箱6 = "xxx@163.com"
    邮箱1授权码 = "11111"
    邮箱2授权码 = "11111"
    邮箱3授权码 = "11111"
    邮箱4授权码 = "11111"
    邮箱5授权码 = "11111"
    邮箱6授权码 = "11111"
    user_email_address = "xxx@qq.com"  # 接收邮箱仅限qq
    user_password = "111"
    pop_server_host = 'pop.qq.com'
    pop_server_port = 995
DEBUG = False  # 设置为 True 开启调试模式
设备号 = "未知"
极限模式=0 # 0不开启  #1开启
设备 = 1  # 0其他  #1红手指,
箱子 = 3  # 0不开启  #1开启陆战 #2开启海战 #3全开
赛季任务 = 0  # 0不开启  #1开启 ##2活动任务
日常任务 = 1  # 0不开启  #1开启
用户间隔时间 = 1  # 战斗次数
间隔时间 = 1
加速器 = 2  # 1biubiu #2 clash
单次游戏局数 = 10
随机战斗模式 = 1  # 为百分比 1 为100%海战
战斗模式 = 2  # 1 海战图色识别 #2 海战Ai #3空战图色识别
自动继续时间 = 60
是否接受bug信息用户 = 1  # 0接受  #1不接受
是否接受bug信息控制 = 0  # 0接受  #1不接受
蓝图 = 1  # 0不开启  #1开启
是否切换载具=1 # 0不开启  #1开启

if 模式==1:
    数据位置 = '/storage/emulated/0/Download/参数.txt'
else:
    数据位置='/storage/emulated/0/airscript/model/战雷/参数.txt'

if "导入模块":
    # 创建Yolov5 并加载模型文件
    from ascript.android.screen import YoLov5, FindImages, Ocr, FindColors
    from ascript.android.ui import Dialog
    from ascript.android.system import R
    from airscript.node import Selector
    from airscript.intent import Intent
    from airscript.action import key, slide, click
    from airscript.screen import Screen
    from airscript.system import Device
    from ascript.android import system
    import time

    import asyncio
    import ctypes
    import email
    import imaplib
    import math
    import multiprocessing
    import random
    import requests
    import shutil
    import smtplib
    import time
    from datetime import datetime, timedelta
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.header import decode_header
    from threading import Thread
    from ascript.android import action
    from ascript.android.system import R
    from ascript.android.screen import Ocr
    from ascript.android.screen import FindColors
    import os

    # 检查文件是否存在
    # if not os.path.exists('/storage/emulated/0/airscript/model/战雷/参数.txt'):
    #     # 如果文件不存在，创建文件并写入第一行到第15行的内容为1
    #     with open('/storage/emulated/0/airscript/model/战雷/参数.txt', 'w') as 文件:
    #         for _ in range(15):
    #             文件.write('0\n')
    #
    # # 其他代码...

    def is_valid_int_regex(s):
        aaasd = int(float(s))
        log(aaasd)
        return aaasd


    def log(*messages):
        if DEBUG:
            formatted_messages = [str(message) for message in messages]
            print(" | ".join(formatted_messages))


    def read_and_set_values():
        global 首次,DEBUG, 是否首次, 极限模式,日常任务,用户间隔时间, 时长, 时长小时, 时长分钟, 时长小时0, 是否接受bug信息用户, 时长分钟0, 设备号, 用户邮箱, 箱子, 自动继续时间, 单次游戏局数, 随机战斗模式, 战斗模式, 是否切换载具
        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
        try:
            log(f"开始读取文件")
            with open(file_path, "r+") as file:
                lines = file.readlines()
                log(lines[0])

                if lines[0] == '1\n':
                    是否首次 = 1
                    log("载入数据")
                    Dialog.toast('载入数据 ')
                    DEBUG = False
                    首次 = lines[0].strip()
                    时长 = is_valid_int_regex(lines[1].strip())
                    时长小时0 = is_valid_int_regex(lines[2].strip())
                    时长分钟0 = is_valid_int_regex(lines[3].strip())
                    设备号 = lines[4].strip()
                    用户邮箱 = lines[5].strip()
                    箱子 = int(lines[6].strip())
                    用户间隔时间 = int(lines[7].strip())
                    自动继续时间 = int(lines[8].strip())
                    单次游戏局数 = int(lines[9].strip())
                    随机战斗模式 = float(lines[10].strip())
                    战斗模式 = int(lines[11].strip())
                    是否接受bug信息用户 = int(lines[12].strip())
                    极限模式= int(lines[13].strip())
                    日常任务= int(lines[14].strip())
                    是否切换载具= int(lines[15].strip())

                    log(lines[0].strip(), is_valid_int_regex(lines[1].strip()), is_valid_int_regex(lines[2].strip()),
                        is_valid_int_regex(lines[3].strip()), lines[4].strip(), lines[5].strip())

                else:
                    是否首次 = 0
                    log("保存数据")
                    Dialog.toast('保存数据 ')
                    lines[0] = '1\n'
                    lines[1] = f'{时长}\n'
                    lines[2] = f'{时长小时0}\n'
                    lines[3] = f'{时长分钟0}\n'
                    lines[4] = f'{设备号}\n'
                    lines[5] = f'{用户邮箱}\n'
                    lines[6] = f'{箱子}\n'
                    lines[7] = f'{用户间隔时间}\n'
                    lines[8] = f'{自动继续时间}\n'
                    lines[9] = f'{单次游戏局数}\n'
                    lines[10] = f'{随机战斗模式}\n'
                    lines[11] = f'{战斗模式}\n'
                    lines[12] = f'{是否接受bug信息用户}\n'
                    # lines[12] = "时长\n 时长小时0\n 时长分钟0\n 设备号\n 用户邮箱\n 箱子\n 用户间隔时间\n 自动继续时间\n 单次游戏局数\n 随机战斗模式\n 战斗模式"
                    lines[13] = f'{极限模式}\n'
                    lines[14] = f'{日常任务}\n'
                    lines[15] = f'{是否切换载具}\n'
                    log(lines[0].strip(), is_valid_int_regex(lines[1].strip()), is_valid_int_regex(lines[2].strip()),
                        is_valid_int_regex(lines[3].strip()), lines[4].strip(), lines[5].strip())

                    file.seek(0)
                    file.writelines(lines)

        except FileNotFoundError:
            log(f"文件未找到: {file_path}")
        except Exception as e:
            log(f"发生错误: {e}")

    def 输入数据():
        global 首次,DEBUG, 是否首次, 极限模式,日常任务,用户间隔时间, 时长, 时长小时, 时长分钟, 时长小时0, 是否接受bug信息用户, 时长分钟0, 设备号, 用户邮箱, 箱子, 自动继续时间, 单次游戏局数, 随机战斗模式, 战斗模式, 是否切换载具
        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
        try:
            log(f"开始读取文件")
            with open(file_path, "r+") as file:
                lines = file.readlines()
                log(lines[0])
                if lines[0] == '1\n':
                    是否首次 = 1
                    log("载入数据")

                else:
                    是否首次 = 0

                    file.seek(0)
                    file.writelines(lines)

        except FileNotFoundError:
            log(f"文件未找到: {file_path}")
        except Exception as e:
            log(f"发生错误: {e}")
    def save_duration(天, 小时, 分钟):
        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
        try:
            with open(file_path, "r+") as file:
                lines = file.readlines()

                lines[1] = f"{int(float(天))}\n"
                lines[2] = f"{int(float(小时))}\n"
                lines[3] = f"{int(float(分钟))}\n"
                lines[0] = '1\n'

                file.seek(0)
                file.writelines(lines)

        except FileNotFoundError:
            log(f"文件未找到: {file_path}")
        except Exception as e:
            log(f"发生错误: {e}")


    def 重置时间():
        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
        try:
            with open(file_path, "r+") as file:
                lines = file.readlines()

                lines[1] = f"10\n"
                lines[2] = f"10\n"
                lines[3] = f"10\n"
                lines[0] = '1\n'

                file.seek(0)
                file.writelines(lines)

        except FileNotFoundError:
            log(f"文件未找到: {file_path}")
        except Exception as e:
            log(f"发生错误: {e}")

if "开始参数":
    display = Device.display()
    xg = display.heightPixels
    xk = display.widthPixels
    # # 获取屏幕高度(像素)
    log(display.heightPixels)
    # # 获取屏幕宽度(像素)
    log(display.widthPixels)
    ##屏幕密度
    log(display.density)
    # 测试机型 1600X720
    log("版本号:",版本)
    cg = 720
    ck = 1280


if "定义参数":
    ting = 4 + 3 * random.random()
    timg = 0.5 + 3 * random.random()
    xa = 447
    chishuyou = 用户间隔时间
    chishuyou1 = 间隔时间
    邮箱控制 = 0
    更新shu=0
    海1空2=0
    重启了 = 0
    上次是海1空2 = 1
    识别x = 0
    现次数 = 0
    崩溃次数 = 0
    游戏崩溃 = 0
    邮箱控制2 = 0
    正在匹配游戏 = 0
    识别y = 0
    总消耗时长小时 = 0
    加速器节点 = 1
    总消耗时长分钟 = 0
    随机战斗模式字 = "未知模式"
    时长秒 = 0
    bb = 1
    是否接受bug信息用户字 = "未知"
    游戏结束 = 0
    管理邮件编号 = 1
    邮件编号 = 1
    总暂停小时 = 0
    总暂停分钟 = 0
    总暂停天 = 0
    总暂停时长 = 0
    xunhuanshu = 9999999990000
    无法识别 = 0
    完成程度 = 0
    restarts = 0
    dhdh = 0
    jinbi = 0
    jinbi5 = 0
    jinbi7 = 0
    jinbi15 = 0
    piao10 = 0
    piao20 = 0
    piao100 = 0
    yingbi1000 = 0
    yingbi1500 = 0
    yingbi3000 = 0
    ajinbi = 0
    ajinbi5 = 0
    ajinbi7 = 0
    ajinbi15 = 0
    apiao10 = 0
    apiao20 = 0
    apiao100 = 0
    ayingbi1000 = 0
    ayingbi1500 = 0
    ayingbi3000 = 0
    affaf = 0
    liangci = 0
    ju = 0
    jinbici = 0
    aafaf = 0
    aafaf1 = 0
    miaohuoci = 0
    yinbici = 0
    xiulici = 0
    piaoci = 0
    yanwuci = 0
    qitaci = 0
    jinbia = 0
    piaoa = 0
    yinbia = 0
    xiulia = 0
    yanwua = 0
    miaohuoa = 0
    qitaa = 0
    whole_seconds = 0
    miaohuo = 0
    是否强行登录=0
    yinbi = 0
    xiuli = 0
    yanwu = 0
    piao = 0
    chi = 0
    qita = 0
    a1aa = 1
    左右判断 = 1
    day = 1
    hour = 1
    minute = 1
    second = 1
    hours = 1
    minutes = 1
    secs = 1
    jinbiold = 0
    yinbiold = 0
    piaoold = 0
    cuowuci = 0
    重启过 = 0
    网络问题 = 0
    邮箱选择 = 1
    bug数 = 0
    bug时间 = 0
    战斗模式字 = 0
    玩家名 = "无法识别"
    进入游戏空_bug = 0
    进入游戏海_bug = 0
    赛季任务_bug = 0
    去宝箱界面_bug = 0
    服务器_bug = 0
    海战 = 0
    海战_bug = 0
    海战ai_bug = 0
    空战 = 0
    战斗空_bug = 0
    锁定x = 92
    锁定y = 494

if "邮箱":
    import imaplib
    import email
    from email.header import decode_header
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import smtplib
    import threading
    from email.parser import Parser
    from email.header import decode_header
    from email.utils import parseaddr
    from datetime import datetime, timedelta
    import re

    if "邮箱发送":
        def email_souduo111(from_email, password):
            try:
                mail = imaplib.IMAP4_SSL('imap.163.com')
                mail.login(from_email, password)
                mail.select('inbox')

                status, data = mail.search(None, 'ALL')
                mail_ids = data[0]
                id_list = mail_ids.split()
                for num in id_list:
                    status, data = mail.fetch(num, '(RFC822)')
                    msg = email.message_from_bytes(data[0][1])
                    email_subject = decode_header(msg['subject'])[0][0]
                    if isinstance(email_subject, bytes):
                        email_subject = email_subject.decode()
                    email_from = decode_header(msg['from'])[0][0]
                    if isinstance(email_from, bytes):
                        email_from = email_from.decode()
                    log(f'From: {email_from}\nSubject: {email_subject}\n')

                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == 'text/plain':
                                email_body = part.get_payload(decode=True).decode()
                                log(f'Body: {email_body}\n')
                    else:
                        email_body = msg.get_payload(decode=True).decode()
                        log(f'Body: {email_body}\n')

                mail.logout()
            except Exception as e:
                log(f'Failed to connect with {from_email}: {e}')


        import logging


        def email_souduo(from_email, password):
            try:
                # 使用上下文管理器自动关闭连接
                with imaplib.IMAP4_SSL('imap.163.com') as mail:
                    mail.login(from_email, password)
                    mail.select('inbox')

                    # 搜索所有邮件
                    status, data = mail.search(None, 'ALL')
                    if status != "OK":
                        logging.error("Failed to search inbox.")
                        return

                    mail_ids = data[0].split()
                    logging.info(f"Total emails: {len(mail_ids)}")

                    for num in mail_ids:
                        status, data = mail.fetch(num, '(RFC822)')
                        if status != "OK":
                            logging.error(f"Failed to fetch email ID {num}.")
                            continue

                        # 解析邮件
                        msg = email.message_from_bytes(data[0][1])
                        subject = decode_header(msg.get("subject"))[0][0]
                        subject = subject.decode() if isinstance(subject, bytes) else subject
                        sender = decode_header(msg.get("from"))[0][0]
                        sender = sender.decode() if isinstance(sender, bytes) else sender

                        logging.info(f"From: {sender}\nSubject: {subject}")

                        # 获取邮件正文
                        body = None
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode(errors="ignore")
                                    break
                        else:
                            body = msg.get_payload(decode=True).decode(errors="ignore")

                        logging.info(f"Body: {body}\n")

                    mail.logout()
            except imaplib.IMAP4.error as e:
                logging.error(f"IMAP error: {e}")
            except Exception as e:
                logging.error(f"An error occurred: {e}")
        def email_sou():
            from_email1 = f'{发送邮箱1}'
            password1 = f'{邮箱1授权码}'

            from_email2 = f'{发送邮箱2}'
            password2 = f'{邮箱2授权码}'

            from_email3 = f'{发送邮箱3}'
            password3 = f'{邮箱3授权码}'

            from_email4 = f'{发送邮箱4}'
            password4 = f'{邮箱4授权码}'

            from_email5 = f'{发送邮箱5}'
            password5 = f'{邮箱5授权码}'

            from_email6 = f'{发送邮箱6}'
            password6 = f'{邮箱6授权码}'

            while True:
                try:
                    email_souduo(from_email1, password1)
                except Exception:
                    try:
                        email_souduo(from_email2, password2)
                    except Exception:
                        try:
                            email_souduo(from_email3, password3)
                        except Exception:
                            try:
                                email_souduo(from_email4, password4)
                            except Exception:
                                try:
                                    email_souduo(from_email5, password5)
                                except Exception:
                                    try:
                                        email_souduo(from_email6, password6)
                                    except Exception:
                                        log(f'Failed to connect with both emails: {e}')

                # 每 15 秒检测一次
                time.sleep(15)


        def email_songduo11(subject, body, to_email, from_email, password):
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            try:
                server = smtplib.SMTP_SSL('smtp.163.com', 465)
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())
                server.quit()

                log(f'邮件从 {from_email} 发送到 {to_email} 成功')
                return True
            except Exception as e:
                log(f'邮件从 {from_email} 发送到 {to_email} 失败: {e}')
                return False


        def email_songduo(subject, body, to_email, from_email, password):
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            try:
                # 使用上下文管理器自动处理关闭连接
                with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
                    server.login(from_email, password)
                    server.sendmail(from_email, to_email, msg.as_string())
                    log(f'邮件从 {from_email} 发送到 {to_email} 成功')
                    return True
            except Exception as e:
                log(f'邮件从 {from_email} 发送到 {to_email} 失败: {e}')
                return False


        def email_song(subject, body, to_email, 指定邮箱=0):
            global 邮箱选择
            from_email1 = f'{发送邮箱1}'
            password1 = f'{邮箱1授权码}'
            if f'{发送邮箱1}' !="xxx@163.com":
                from_email2 = f'{发送邮箱2}'
                password2 = f'{邮箱2授权码}'

                from_email3 = f'{发送邮箱3}'
                password3 = f'{邮箱3授权码}'

                from_email4 = f'{发送邮箱4}'
                password4 = f'{邮箱4授权码}'

                from_email5 = f'{发送邮箱5}'
                password5 = f'{邮箱5授权码}'

                from_email6 = f'{发送邮箱6}'
                password6 = f'{邮箱6授权码}'
            else:
                from_email2 = 'xxx@163.com'
                password2 = '11111'

                from_email3 = 'xxx@163.com'
                password3 = '11111'

                from_email4 = 'xxx@163.com'
                password4 = '11111'

                from_email5 = 'xxx@163.com'
                password5 = '11111'

                from_email6 = 'xxx@163.com'
                password6 = '11111'



            try:
                if 指定邮箱 == 0:
                    if 邮箱选择 == 1:
                        if email_songduo(subject, body, to_email, from_email1, password1):
                            return
                    elif 邮箱选择 == 2:
                        if email_songduo(subject, body, to_email, from_email2, password2):
                            return
                    elif 邮箱选择 == 3:
                        if email_songduo(subject, body, to_email, from_email3, password3):
                            return
                    elif 邮箱选择 == 4:
                        if email_songduo(subject, body, to_email, from_email4, password4):
                            return
                    elif 邮箱选择 == 5:
                        if email_songduo(subject, body, to_email, from_email5, password5):
                            return
                    elif 邮箱选择 == 6:
                        if email_songduo(subject, body, to_email, from_email6, password6):
                            return

                    if not email_songduo(subject, body, to_email, from_email1, password1):
                        邮箱选择 = 2
                        if not email_songduo(subject, body, to_email, from_email2, password2):
                            邮箱选择 = 3
                            if not email_songduo(subject, body, to_email, from_email3, password3):
                                邮箱选择 = 4
                                if not email_songduo(subject, body, to_email, from_email4, password4):
                                    邮箱选择 = 5
                                    if not email_songduo(subject, body, to_email, from_email5, password5):
                                        邮箱选择 = 6
                                        if not email_songduo(subject, body, to_email, from_email6, password6):
                                            pass

                    else:
                        邮箱选择 = 1
                else:
                    if 指定邮箱 == 1:
                        if email_songduo(subject, body, to_email, from_email1, password1):
                            return
                    elif 指定邮箱 == 2:
                        if email_songduo(subject, body, to_email, from_email2, password2):
                            return
                    elif 指定邮箱 == 3:
                        if email_songduo(subject, body, to_email, from_email3, password3):
                            return
                    elif 指定邮箱 == 4:
                        if email_songduo(subject, body, to_email, from_email4, password4):
                            return
                    elif 指定邮箱 == 5:
                        if email_songduo(subject, body, to_email, from_email5, password5):
                            return
                    elif 指定邮箱 == 6:
                        if email_songduo(subject, body, to_email, from_email6, password6):
                            return
                    if 邮箱选择 == 1:
                        if email_songduo(subject, body, to_email, from_email1, password1):
                            return
                    elif 邮箱选择 == 2:
                        if email_songduo(subject, body, to_email, from_email2, password2):
                            return
                    elif 邮箱选择 == 3:
                        if email_songduo(subject, body, to_email, from_email3, password3):
                            return
                    elif 邮箱选择 == 4:
                        if email_songduo(subject, body, to_email, from_email4, password4):
                            return
                    elif 邮箱选择 == 5:
                        if email_songduo(subject, body, to_email, from_email5, password5):
                            return
                    elif 邮箱选择 == 6:
                        if email_songduo(subject, body, to_email, from_email6, password6):
                            return

                    if not email_songduo(subject, body, to_email, from_email1, password1):
                        邮箱选择 = 2
                        if not email_songduo(subject, body, to_email, from_email2, password2):
                            邮箱选择 = 3
                            if not email_songduo(subject, body, to_email, from_email3, password3):
                                邮箱选择 = 4
                                if not email_songduo(subject, body, to_email, from_email4, password4):
                                    邮箱选择 = 5
                                    if not email_songduo(subject, body, to_email, from_email5, password5):
                                        邮箱选择 = 6
                                        if not email_songduo(subject, body, to_email, from_email6, password6):
                                            pass
                    else:
                        邮箱选择 = 1



            except Exception as e:
                log(f'Failed to send email with both accounts: {e}')

    # 使用示例
    # email_song('测试邮件', '这是一封测试邮件', 'recipient_email@example.com')
    if "邮箱接收":

        import pytz

        from dateutil import parser

        from datetime import datetime, timedelta
        import pytz
        import poplib

        # 创建事件对象，用于线程间通信
        stop_event = threading.Event()
        continue_event = threading.Event()

        # 记录已处理的邮件 ID
        processed_mail_ids = set()

        # 计算5分钟前的时间
        # five_minutes_ago = datetime.now() - timedelta(minutes=5)
        # 获取当前时间并添加时区信息
        tz = pytz.timezone('Asia/Shanghai')
        five_minutes_ago = datetime.now(tz) - timedelta(minutes=5)


        def connect_email_by_pop3():
            email_server = None
            last_login_time = datetime.now()

            while True:
                if email_server is None or (datetime.now() - last_login_time) >= timedelta(hours=1):
                    try:
                        # 如果超过1小时，重新连接并登录
                        if email_server:
                            email_server.quit()  # 断开现有连接
                            email_server = None

                        # 连接到邮件服务器
                        email_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
                        log("连接pop服务器-------正常，开始验证用户邮箱")

                        # 验证用户邮箱
                        email_server.user(user_email_address)
                        log("用户邮箱验证-------正常，开始验证邮箱授权码")

                        # 验证邮箱密码是否正确，注意不是登录密码，是授权码
                        email_server.pass_(user_password)
                        log("邮箱授权码验证-------正常，开始接受邮箱以及附件")

                        last_login_time = datetime.now()  # 更新上次登录时间

                    except Exception as e:
                        log(f"连接或操作pop服务器时出现异常: {e}")
                        email_server = None
                        time.sleep(60)  # 等待60秒后重试
                        continue

                try:
                    # 处理邮箱相关信息
                    parse_email_server(email_server)

                except Exception as e:
                    log(f"解析邮件时出现异常: {e}")
                    # 如果出现异常，重新连接
                    email_server = None

                # 等待10秒后再次检查邮件
                time.sleep(50)


        def parse_email_server(email_server):
            try:
                resp, mails, octets = email_server.list()
                num, total_size = email_server.stat()
                # log("邮件数量为：" + str(num))
                index = len(mails)
                for i in range(index, 0, -1):
                    resp, lines, octets = email_server.retr(i)
                    msg_content = b'\r\n'.join(lines)

                    # 检查邮件内容是否为空
                    if not msg_content:
                        log("邮件内容为空，跳过解析")
                        continue

                    try:
                        msg_content = msg_content.decode('utf-8')
                    except UnicodeDecodeError:
                        try:
                            msg_content = msg_content.decode('latin-1')
                        except UnicodeDecodeError:
                            try:
                                msg_content = msg_content.decode('iso-8859-1')
                            except UnicodeDecodeError:
                                log("无法解码邮件内容，跳过解析")
                                continue  # 跳过解析

                    if not msg_content:  # 再次检查是否解码成功
                        log("解码后的邮件内容仍然为空，跳过解析")
                        continue

                    msg = Parser().parsestr(msg_content)
                    if not msg:
                        log("解析邮件内容时返回None，跳过解析")
                        continue

                    mail_datetime = parse_mail_time(msg.get("date"))
                    if mail_datetime < five_minutes_ago:
                        continue  # 忽略5分钟前的邮件

                    mail_id = str(i)
                    if mail_id in processed_mail_ids:
                        continue  # 忽略已处理的邮件

                    processed_mail_ids.add(mail_id)  # 记录邮件 ID
                    max_mail_time_str = mail_datetime.strftime("%Y-%m-%d %H:%M")
                    log("邮件接收时间为：" + max_mail_time_str)
                    parser_content(msg, 0)
            except Exception as e:
                log(f"解析邮件时出现异常: {e}")


        def is_https_link(subject):
            pattern = r'https://[\w\./]+\.zip'
            return bool(re.match(pattern, subject))


        def extract_numbers(text):
            # 使用正则表达式匹配数字
            numbers = re.findall(r'\d+', text)

            # 将匹配到的数字转换为整数
            int_numbers = [int(num) for num in numbers]

            return int_numbers


        def contains_update_code(string):
            pattern = r'更新代码\s*\d+'
            return bool(re.search(pattern, string))


        def parser_content(msg, indent):
            global 时长,极限模式, 用户间隔时间, 赛季任务, 自动继续时间, 版本, 是否接受bug信息用户,日常任务, 任务, 时长小时0, 时长分钟0, 时长, 时长小时, 时长分钟, 时长小时0, 时长分钟0, 设备号, 用户邮箱, 用户间隔时间, 间隔时间, 箱子, 单次游戏局数, 随机战斗模式, 战斗模式
            if indent == 0:
                parser_email_header(msg)

            sender_email = parseaddr(msg['From'])[1]
            subject = str(decode_str(msg.get("Subject")))
            内容_email = "无法解析"

            try:
                if msg.get_content_maintype() == 'multipart':
                    for part in msg.get_payload():
                        if part.get_content_maintype() == 'text':
                            内容_email = part.get_payload(decode=True).decode('utf-8')
                            break
                elif msg.get_content_maintype() == 'text':
                    内容_email = msg.get_payload(decode=True).decode('utf-8')

                log(内容_email)
            except Exception as e:
                log(f"邮件内容解析失败: {e}")
            新版本 = 版本 + 0.1
            新版本1 = 版本 + 0.01
            新版本2 = 版本 + 1
            result_new = "未知"
            if sender_email == "t--yang-only@outlook.com":
                if contains_update_code(subject):
                    result_new = subject.split("更新代码")[1]
                    result_new = float(result_new)
                    if result_new > 版本:
                        # if f"更新代码{result_new}" in subject:  # or f"更新代码{新版本1}" in subject or f"更新代码{新版本2}" in subject

                        if True:
                            url = 内容_email
                            save_path = "/storage/emulated/0/airscript/model/战雷/__init__.py"
                            max_retries = 5  # 最大重试次数
                            retry_delay = 5  # 重试间隔时间（秒）
                            chunk_size = 1024  # 每次读取的字节数
                            progress_interval = 5  # 进度反馈间隔（秒）

                            retries = 0
                            while retries < max_retries:
                                response = None
                                try:
                                    response = requests.get(url, stream=True, timeout=60)  # 增加超时时间
                                    if response.status_code == 200:
                                        total_size = int(response.headers.get('content-length', 0))
                                        downloaded_size = 0
                                        last_progress_time = time.time()
                                        with open(save_path, 'wb') as out_file:
                                            for data in response.iter_content(chunk_size=chunk_size):
                                                if data:
                                                    out_file.write(data)
                                                    downloaded_size += len(data)
                                                    current_time = time.time()
                                                    if current_time - last_progress_time >= progress_interval:
                                                        log(
                                                            f"下载进度: {downloaded_size / total_size * 100:.2f}%")
                                                        last_progress_time = current_time
                                        log(f"APK文件已成功下载并保存到: {save_path}")
                                        stop_event.set()  # 设置停止事件，通知主线程停止
                                        continue_event.clear()  # 清除继续事件
                                        email_song(
                                            f'{用户邮箱},网络更新脚本成功,升级为 {result_new},原版本 {版本},{设备号}',
                                            f'网络更新脚本成功,脚本升级为 {result_new}', f't--yang-only@outlook.com', 4)
                                        email_song(f'网络更新脚本成功,升级为 {result_new},原版本 {版本}',
                                                   f'网络更新脚本成功,脚本升级为 {result_new}',
                                                   f'{用户邮箱}', 4)
                                        版本 = result_new
                                        重启()
                                        system.reboot(15000)
                                        return  # 下载成功，退出循环
                                    else:
                                        log(f"下载失败，HTTP状态码: {response.status_code}")
                                        break  # 下载失败，退出循环
                                except requests.exceptions.RequestException as e:
                                    log(f"下载过程中发生错误: {e}")
                                    retries += 1
                                    if retries < max_retries:
                                        log(f"重试下载，第 {retries} 次，等待 {retry_delay} 秒...")
                                        time.sleep(retry_delay)
                                    else:
                                        log("已达到最大重试次数，下载失败。")
                                        email_song(f'{用户邮箱},网络更新脚本失败,{设备号}',
                                                   f'网络更新脚本失败', f't--yang-only@outlook.com', 4)
                                        email_song('网络更新脚本失败',
                                                   f'网络更新脚本失败',
                                                   f'{用户邮箱}', 4)
                                        return
                                finally:
                                    if response is not None:
                                        response.close()

                                return

                        # email_song(f'{用户邮箱},网络更新脚本失败,{设备号}',
                        #            f'网络更新脚本失败', f't--yang-only@outlook.com', 4)
                        # email_song('网络更新脚本失败',
                        #            f'网络更新脚本失败',
                        #            f'{用户邮箱}', 4)
                        # time.sleep(1)
                        #
                        # import os
                        # import zipfile

                        #
                        # def extract_zip(file_path, password):
                        #     with zipfile.ZipFile(file_path) as zf:
                        #         for file in zf.namelist():
                        #             if not os.path.exists(file):
                        #                 zf.extract(file, path='.', pwd=password.encode('utf-8'))
                        #
                        #
                        # zip_file_path = "/storage/emulated/0/airscript/model/源码.zip"
                        # password = "788206=*-*"
                        #
                        # # Get the directory of the ZIP file
                        # extract_dir = os.path.dirname(zip_file_path)
                        #
                        # extract_zip(zip_file_path, password)
                        faf

                if "间隔时间" in subject:
                    try:
                        x = subject.split("间隔时间")[1].strip()
                        间隔时间 = x
                        email_song('收件间隔时间',
                                   f"收件间隔时间设置{x}局一次",
                                   f't--yang-only@outlook.com', 4)

                    except IndexError:
                        pass
                if subject.startswith(f"{用户邮箱}时长"):
                    try:
                        # 提取时长值

                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                log(lines[0])

                                if lines[0] == '1\n':
                                    log("载入数据")
                                    时长 = is_valid_int_regex(lines[1].strip())
                                    时长小时0 = is_valid_int_regex(lines[2].strip())
                                    时长分钟0 = is_valid_int_regex(lines[3].strip())

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        time_value_str = subject.split(f"{用户邮箱}时长")[1]
                        time_value = int(time_value_str)
                        增时长天 = 0
                        增时长小时 = 0
                        增时长分钟 = 0
                        if time_value > 0:
                            增时长天 = time_value // 24
                            增时长小时 = (time_value % 24) // 1
                            增时长分钟 = ((time_value % 24) % 1) * 60
                        else:
                            time_value = -time_value
                            增时长天 -= time_value // 24
                            增时长小时 -= (time_value % 24) // 1
                            增时长分钟 -= ((time_value % 24) % 1) * 60

                        # 转换为整数，支持负数
                        时长 += 增时长天
                        时长小时0 += 增时长小时
                        时长分钟0 += 增时长分钟
                        时长小时0 += (时长 % 1) * 24
                        时长 = 时长 // 1
                        时长分钟0 += (时长小时0 % 1) * 60
                        时长小时0 += 时长分钟0 // 60
                        时长 += 时长小时0 // 24
                        时长小时0 = 时长小时0 / 1
                        时长分钟0 = 时长分钟0 / 1

                        save_duration(时长, 时长小时0, 时长分钟0)

                        if time_value > 0:

                            email_song(f'{用户邮箱},增加时长,批量命令,{设备号}',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f't--yang-only@outlook.com', 4)
                            email_song('增加时长,批量命令',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                        else:
                            email_song(f'{用户邮箱},减少时长,批量命令,{设备号}',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f't--yang-only@outlook.com', 4)
                            email_song('减少时长,批量命令',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天,{时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析时长值，忽略此命令")  # 如果发件人不是用户邮箱，忽略这封邮件
                if subject.startswith("all时长"):

                    try:
                        # 提取时长值

                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                log(lines[0])

                                if lines[0] == '1\n':
                                    log("载入数据")
                                    时长 = is_valid_int_regex(lines[1].strip())
                                    时长小时0 = is_valid_int_regex(lines[2].strip())
                                    时长分钟0 = is_valid_int_regex(lines[3].strip())

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        time_value_str = subject.split("all时长")[1]
                        time_value = int(time_value_str)
                        增时长天 = 0
                        增时长小时 = 0
                        增时长分钟 = 0
                        if time_value > 0:
                            增时长天 = time_value // 24
                            增时长小时 = (time_value % 24) // 1
                            增时长分钟 = ((time_value % 24) % 1) * 60
                        else:
                            time_value = -time_value
                            增时长天 -= time_value // 24
                            增时长小时 -= (time_value % 24) // 1
                            增时长分钟 -= ((time_value % 24) % 1) * 60

                        # 转换为整数，支持负数
                        时长 += 增时长天
                        时长小时0 += 增时长小时
                        时长分钟0 += 增时长分钟
                        时长小时0 += (时长 % 1) * 24
                        时长 = 时长 // 1
                        时长分钟0 += (时长小时0 % 1) * 60
                        时长小时0 += 时长分钟0 // 60
                        时长 += 时长小时0 // 24
                        时长小时0 = 时长小时0 / 1
                        时长分钟0 = 时长分钟0 / 1

                        save_duration(时长, 时长小时0, 时长分钟0)

                        if time_value > 0:

                            email_song(f'{用户邮箱},增加时长,批量命令,{设备号}',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f't--yang-only@outlook.com', 4)
                            email_song('增加时长,批量命令',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                        else:
                            email_song(f'{用户邮箱},减少时长,批量命令,{设备号}',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f't--yang-only@outlook.com', 4)
                            email_song('减少时长,批量命令',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天,{时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析时长值，忽略此命令")  # 如果发件人不是用户邮箱，忽略这封邮件
                if subject.startswith(f"{用户邮箱}重启") or subject.startswith("all重启"):
                    stop_event.set()  # 设置停止事件，通知主线程停止
                    continue_event.clear()
                    time.sleep(60)  # 清除继续事件
                    启动()
                    stop_event.clear()  # 清除停止事件状态
                    continue_event.set()  # 设置继续事件，重新启动任务

                    email_song(f'{用户邮箱},{设备号}执行重启', f't--yang-only@outlook.com', 4)
                    email_song('执行操作', "执行重启" f'{用户邮箱}', 4)

                if f"{用户邮箱}停止" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split(f"{用户邮箱}停止")[1].strip()
                        stop_action(x)  # 传递时间参数
                    except IndexError:
                        stop_action()
                if "all停止" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split("all停止")[1].strip()
                        stop_action(x)  # 传递时间参数
                    except IndexError:
                        stop_action()

                if subject.startswith(f"{用户邮箱}继续") or subject.startswith("all继续"):
                    continue_action()
                if f"{用户邮箱}赛季任务关" in subject or "all赛季任务关" in subject:
                    赛季任务 = 0
                    email_song(f'{用户邮箱}停止赛季任务{设备号}', '停止赛季任务', f't--yang-only@outlook.com', 4)
                    email_song('执行操作', "停止赛季任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}赛季任务开" in subject or "all赛季任务开" in subject:
                    赛季任务 = 1
                    email_song(f'{用户邮箱}{设备号}', '执行赛季任务', f't--yang-only@outlook.com', 4)
                    email_song('执行操作', "执行赛季任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}活动任务关" in subject or "all活动任务关" in subject:
                    赛季任务 = 0
                    email_song(f'{用户邮箱}停止活动任务{设备号}', '停止活动任务', f't--yang-only@outlook.com', 4)
                    email_song('执行操作', "停止活动任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}活动任务开" in subject or "all活动任务开" in subject:
                    赛季任务 = 1
                    email_song(f'{用户邮箱}{设备号}', '执行活动任务', f't--yang-only@outlook.com', 4)
                    email_song('执行操作', "执行活动任务", f'{用户邮箱}', 4)

                if f"{用户邮箱}接受bug信息" in subject or "all接受bug信息" in subject:
                    是否接受bug信息用户 = 0
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[12] = f'{是否接受bug信息用户}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱}设置接受bug信息{设备号}', '接受bug信息用户', f't--yang-only@outlook.com', 4)
                    email_song('执行操作,置接受bug信息', "接受bug信息用户", f'{用户邮箱}', 4)
                if f"{用户邮箱}不接受bug信息" in subject or "all不接受bug信息" in subject:
                    是否接受bug信息用户 = 1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[12] = f'{是否接受bug信息用户}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱}设置不接受bug信息{设备号}', '不接受bug信息用户', f't--yang-only@outlook.com', 4)
                    email_song('执行操作,设置不接受bug信息', "不接受bug信息用户", f'{用户邮箱}', 4)
                if f"{用户邮箱}日常任务开" in subject or "all日常任务开" in subject:
                    日常任务 = 1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[14] = f'{日常任务}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱},{设备号}设置全托', "将每日执行每日任务", f't--yang-only@outlook.com', 4)
                    email_song('设置全托', "将每日执行每日任务", f'{用户邮箱}', 4)
                else:
                    if f"{用户邮箱}日常任务关" in subject or "all日常任务关" in subject:
                        日常任务 = 0
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[14] = f'{日常任务}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}关闭全托', "停止每日执行每日任务", f't--yang-only@outlook.com', 4)
                        email_song('关闭全托', "停止每日执行每日任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}极限模式开" in subject or "all极限模式开" in subject:
                    极限模式=1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[13] = f'{极限模式}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    log(f"极限模式已修改为: {极限模式}")
                    email_song(f'{用户邮箱},{设备号}设置极限模式', "将执行极限模式", f't--yang-only@outlook.com', 4)
                    email_song('设置极限模式', "将执行极限模式", f'{用户邮箱}', 4)
                else:
                    if f"{用户邮箱}极限模式关" in subject or "all极限模式关" in subject:
                        极限模式=0
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[13] = f'{极限模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        log(f"极限模式已修改为: {极限模式}")
                        email_song(f'{用户邮箱},{设备号}关闭极限模式', "停止极限模式", f't--yang-only@outlook.com', 4)
                        email_song('关闭极限模式', "停止极限模式", f'{用户邮箱}', 4)
                if subject.startswith(f"{用户邮箱}宝箱"):

                    try:
                        # 提取宝箱值
                        宝箱_value_str = subject.split(f"{用户邮箱}宝箱")[1]
                        宝箱_value = int(宝箱_value_str)
                        宝箱 = min(宝箱_value, 3)  # 将宝箱值限制在3以内
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[6] = f'{箱子}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        log(f"宝箱已修改为: {宝箱}")
                        email_song(f'{用户邮箱},{设备号}宝箱设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f't--yang-only@outlook.com', 4)
                        email_song('宝箱购买设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("all宝箱"):
                    try:
                        # 提取宝箱值
                        宝箱_value_str = subject.split("all宝箱")[1]
                        宝箱_value = int(宝箱_value_str)
                        宝箱 = min(宝箱_value, 3)  # 将宝箱值限制在3以内
                        log(f"宝箱已修改为: {宝箱}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[6] = f'{箱子}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}宝箱设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f't--yang-only@outlook.com', 4)
                        email_song('宝箱购买设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("all单次游戏局数"):
                    try:
                        # 提取宝箱值
                        单次游戏局数_value_str = subject.split("all单次游戏局数")[1]
                        单次游戏局数 = int(单次游戏局数_value_str)
                        log(f"单次游戏局数已修改为: {单次游戏局数}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[9] = f'{单次游戏局数}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}单次游戏局数设置,批量命令',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f't--yang-only@outlook.com', 4)
                        email_song('单次游戏局数设置,批量命令',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith(f"{用户邮箱}单次游戏局数"):
                    try:
                        # 提取宝箱值
                        单次游戏局数_value_str = subject.split(f"{用户邮箱}单次游戏局数")[1]
                        单次游戏局数 = int(单次游戏局数_value_str)
                        log(f"单次游戏局数已修改为: {单次游戏局数}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[9] = f'{单次游戏局数}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}单次游戏局数设置',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f't--yang-only@outlook.com', 4)
                        email_song('单次游戏局数设置',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")

                if subject.startswith(f"{用户邮箱}随机战斗模式"):
                    try:
                        # 提取宝箱值
                        随机战斗模式_value_str = subject.split(f"{用户邮箱}随机战斗模式")[1]
                        随机战斗模式 = float(随机战斗模式_value_str)
                        log(f"随机战斗模式已修改为: {随机战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[10] = f'{随机战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}随机战斗模式设置',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f't--yang-only@outlook.com', 4)
                        email_song('随机战斗模式设置',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("all随机战斗模式"):
                    try:
                        # 提取宝箱值
                        随机战斗模式_value_str = subject.split("all随机战斗模式")[1]
                        随机战斗模式 = float(随机战斗模式_value_str)
                        log(f"随机战斗模式已修改为: {随机战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[10] = f'{随机战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}随机战斗模式设置,批量命令',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f't--yang-only@outlook.com', 4)
                        email_song('随机战斗模式设置,批量命令',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")

                if subject.startswith("all战斗模式"):
                    try:
                        # 提取宝箱值
                        战斗模式_value_str = subject.split("all战斗模式")[1]
                        战斗模式 = float(战斗模式_value_str)
                        log(f"战斗模式已修改为: {战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[11] = f'{战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)
                                if 战斗模式 == 1:
                                    战斗模式字 = "识别颜色战斗"
                                elif 战斗模式 == 2:
                                    战斗模式字 = "弱Ai识别战斗"
                                elif 战斗模式 == 3:
                                    战斗模式字 = "空战图色识别"


                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}战斗模式设置,批量命令',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f't--yang-only@outlook.com', 4)
                        email_song('战斗模式设置,批量命令',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith(f"{用户邮箱}战斗模式"):
                    try:
                        # 提取宝箱值
                        战斗模式_value_str = subject.split(f"{用户邮箱}战斗模式")[1]
                        战斗模式 = float(战斗模式_value_str)
                        log(f"战斗模式已修改为: {战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[11] = f'{战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)
                                if 战斗模式 == 1:
                                    战斗模式字 = "识别颜色战斗"
                                elif 战斗模式 == 2:
                                    战斗模式字 = "弱Ai识别战斗"
                                elif 战斗模式 == 3:
                                    战斗模式字 = "空战图色识别"


                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}战斗模式设置',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f't--yang-only@outlook.com', 4)
                        email_song('战斗模式设置',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if f"{用户邮箱}自动继续时间" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split(f"{用户邮箱}自动继续时间")[1]
                        自动继续时间 = int(x)  # 传递时间参数
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[8] = f'{自动继续时间}\n'
                                file.seek(0)
                                file.writelines(lines)
                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f't--yang-only@outlook.com', 4)
                        email_song('设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if "all自动继续时间" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split("all自动继续时间")[1]
                        自动继续时间 = int(x)  # 传递时间参数
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[8] = f'{自动继续时间}\n'
                                file.seek(0)
                                file.writelines(lines)
                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}设置自动继续时间为',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f't--yang-only@outlook.com', 4)
                        email_song('设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
            if sender_email == 报告邮箱:
                if contains_update_code(subject):
                    result_new = subject.split("更新代码")[1]
                    result_new = float(result_new)
                    if result_new > 版本:
                        # if f"更新代码{result_new}" in subject:  # or f"更新代码{新版本1}" in subject or f"更新代码{新版本2}" in subject

                        if True:
                            url = 内容_email
                            save_path = "/storage/emulated/0/airscript/model/战雷/__init__.py"
                            max_retries = 5  # 最大重试次数
                            retry_delay = 5  # 重试间隔时间（秒）
                            chunk_size = 1024  # 每次读取的字节数
                            progress_interval = 5  # 进度反馈间隔（秒）

                            retries = 0
                            while retries < max_retries:
                                response = None
                                try:
                                    response = requests.get(url, stream=True, timeout=60)  # 增加超时时间
                                    if response.status_code == 200:
                                        total_size = int(response.headers.get('content-length', 0))
                                        downloaded_size = 0
                                        last_progress_time = time.time()
                                        with open(save_path, 'wb') as out_file:
                                            for data in response.iter_content(chunk_size=chunk_size):
                                                if data:
                                                    out_file.write(data)
                                                    downloaded_size += len(data)
                                                    current_time = time.time()
                                                    if current_time - last_progress_time >= progress_interval:
                                                        log(
                                                            f"下载进度: {downloaded_size / total_size * 100:.2f}%")
                                                        last_progress_time = current_time
                                        log(f"APK文件已成功下载并保存到: {save_path}")
                                        stop_event.set()  # 设置停止事件，通知主线程停止
                                        continue_event.clear()  # 清除继续事件
                                        email_song(
                                            f'{用户邮箱},网络更新脚本成功,升级为 {result_new},原版本 {版本},{设备号}',
                                            f'网络更新脚本成功,脚本升级为 {result_new}', f'{报告邮箱}', 4)
                                        email_song(f'网络更新脚本成功,升级为 {result_new},原版本 {版本}',
                                                   f'网络更新脚本成功,脚本升级为 {result_new}',
                                                   f'{用户邮箱}', 4)
                                        版本 = result_new
                                        重启()
                                        system.reboot(15000)
                                        return  # 下载成功，退出循环
                                    else:
                                        log(f"下载失败，HTTP状态码: {response.status_code}")
                                        break  # 下载失败，退出循环
                                except requests.exceptions.RequestException as e:
                                    log(f"下载过程中发生错误: {e}")
                                    retries += 1
                                    if retries < max_retries:
                                        log(f"重试下载，第 {retries} 次，等待 {retry_delay} 秒...")
                                        time.sleep(retry_delay)
                                    else:
                                        log("已达到最大重试次数，下载失败。")
                                        email_song(f'{用户邮箱},网络更新脚本失败,{设备号}',
                                                   f'网络更新脚本失败', f'{报告邮箱}', 4)
                                        email_song('网络更新脚本失败',
                                                   f'网络更新脚本失败',
                                                   f'{用户邮箱}', 4)
                                        return
                                finally:
                                    if response is not None:
                                        response.close()

                                return

                        # email_song(f'{用户邮箱},网络更新脚本失败,{设备号}',
                        #            f'网络更新脚本失败', f'{报告邮箱}', 4)
                        # email_song('网络更新脚本失败',
                        #            f'网络更新脚本失败',
                        #            f'{用户邮箱}', 4)
                        # time.sleep(1)
                        #
                        # import os
                        # import zipfile

                        #
                        # def extract_zip(file_path, password):
                        #     with zipfile.ZipFile(file_path) as zf:
                        #         for file in zf.namelist():
                        #             if not os.path.exists(file):
                        #                 zf.extract(file, path='.', pwd=password.encode('utf-8'))
                        #
                        #
                        # zip_file_path = "/storage/emulated/0/airscript/model/源码.zip"
                        # password = "788206=*-*"
                        #
                        # # Get the directory of the ZIP file
                        # extract_dir = os.path.dirname(zip_file_path)
                        #
                        # extract_zip(zip_file_path, password)
                        faf

                if "间隔时间" in subject:
                    try:
                        x = subject.split("间隔时间")[1].strip()
                        间隔时间 = x
                        email_song('收件间隔时间',
                                   f"收件间隔时间设置{x}局一次",
                                   f'{报告邮箱}', 4)

                    except IndexError:
                        pass
                if subject.startswith(f"{用户邮箱}时长"):
                    try:
                        # 提取时长值

                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                log(lines[0])

                                if lines[0] == '1\n':
                                    log("载入数据")
                                    时长 = is_valid_int_regex(lines[1].strip())
                                    时长小时0 = is_valid_int_regex(lines[2].strip())
                                    时长分钟0 = is_valid_int_regex(lines[3].strip())

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        time_value_str = subject.split(f"{用户邮箱}时长")[1]
                        time_value = int(time_value_str)
                        增时长天 = 0
                        增时长小时 = 0
                        增时长分钟 = 0
                        if time_value > 0:
                            增时长天 = time_value // 24
                            增时长小时 = (time_value % 24) // 1
                            增时长分钟 = ((time_value % 24) % 1) * 60
                        else:
                            time_value = -time_value
                            增时长天 -= time_value // 24
                            增时长小时 -= (time_value % 24) // 1
                            增时长分钟 -= ((time_value % 24) % 1) * 60

                        # 转换为整数，支持负数
                        时长 += 增时长天
                        时长小时0 += 增时长小时
                        时长分钟0 += 增时长分钟
                        时长小时0 += (时长 % 1) * 24
                        时长 = 时长 // 1
                        时长分钟0 += (时长小时0 % 1) * 60
                        时长小时0 += 时长分钟0 // 60
                        时长 += 时长小时0 // 24
                        时长小时0 = 时长小时0 / 1
                        时长分钟0 = 时长分钟0 / 1

                        save_duration(时长, 时长小时0, 时长分钟0)

                        if time_value > 0:

                            email_song(f'{用户邮箱},增加时长,批量命令,{设备号}',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{报告邮箱}', 4)
                            email_song('增加时长,批量命令',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                        else:
                            email_song(f'{用户邮箱},减少时长,批量命令,{设备号}',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{报告邮箱}', 4)
                            email_song('减少时长,批量命令',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天,{时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析时长值，忽略此命令")  # 如果发件人不是用户邮箱，忽略这封邮件
                if subject.startswith("all时长"):

                    try:
                        # 提取时长值

                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                log(lines[0])

                                if lines[0] == '1\n':
                                    log("载入数据")
                                    时长 = is_valid_int_regex(lines[1].strip())
                                    时长小时0 = is_valid_int_regex(lines[2].strip())
                                    时长分钟0 = is_valid_int_regex(lines[3].strip())

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        time_value_str = subject.split("all时长")[1]
                        time_value = int(time_value_str)
                        增时长天 = 0
                        增时长小时 = 0
                        增时长分钟 = 0
                        if time_value > 0:
                            增时长天 = time_value // 24
                            增时长小时 = (time_value % 24) // 1
                            增时长分钟 = ((time_value % 24) % 1) * 60
                        else:
                            time_value = -time_value
                            增时长天 -= time_value // 24
                            增时长小时 -= (time_value % 24) // 1
                            增时长分钟 -= ((time_value % 24) % 1) * 60

                        # 转换为整数，支持负数
                        时长 += 增时长天
                        时长小时0 += 增时长小时
                        时长分钟0 += 增时长分钟
                        时长小时0 += (时长 % 1) * 24
                        时长 = 时长 // 1
                        时长分钟0 += (时长小时0 % 1) * 60
                        时长小时0 += 时长分钟0 // 60
                        时长 += 时长小时0 // 24
                        时长小时0 = 时长小时0 / 1
                        时长分钟0 = 时长分钟0 / 1

                        save_duration(时长, 时长小时0, 时长分钟0)

                        if time_value > 0:

                            email_song(f'{用户邮箱},增加时长,批量命令,{设备号}',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{报告邮箱}', 4)
                            email_song('增加时长,批量命令',
                                       f'增加时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                        else:
                            email_song(f'{用户邮箱},减少时长,批量命令,{设备号}',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天, {时长小时0}小时,{时长分钟0}分钟',
                                       f'{报告邮箱}', 4)
                            email_song('减少时长,批量命令',
                                       f'减少时长{增时长天}天, {增时长小时}小时,{增时长分钟}分钟,剩余时长{时长}天,{时长小时0}小时,{时长分钟0}分钟',
                                       f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析时长值，忽略此命令")  # 如果发件人不是用户邮箱，忽略这封邮件
                if subject.startswith(f"{用户邮箱}重启") or subject.startswith("all重启"):
                    stop_event.set()  # 设置停止事件，通知主线程停止
                    continue_event.clear()
                    time.sleep(60)  # 清除继续事件
                    启动()
                    stop_event.clear()  # 清除停止事件状态
                    continue_event.set()  # 设置继续事件，重新启动任务

                    email_song(f'{用户邮箱},{设备号}执行重启', f'{报告邮箱}', 4)
                    email_song('执行操作', "执行重启" f'{用户邮箱}', 4)

                if f"{用户邮箱}停止" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split(f"{用户邮箱}停止")[1].strip()
                        stop_action(x)  # 传递时间参数
                    except IndexError:
                        stop_action()
                if "all停止" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split("all停止")[1].strip()
                        stop_action(x)  # 传递时间参数
                    except IndexError:
                        stop_action()

                if subject.startswith(f"{用户邮箱}继续") or subject.startswith("all继续"):
                    continue_action()
                if f"{用户邮箱}赛季任务关" in subject or "all赛季任务关" in subject:
                    赛季任务 = 0
                    email_song(f'{用户邮箱}停止赛季任务{设备号}', '停止赛季任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "停止赛季任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}赛季任务开" in subject or "all赛季任务开" in subject:
                    赛季任务 = 1
                    email_song(f'{用户邮箱}{设备号}', '执行赛季任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "执行赛季任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}活动任务关" in subject or "all活动任务关" in subject:
                    赛季任务 = 0
                    email_song(f'{用户邮箱}停止活动任务{设备号}', '停止活动任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "停止活动任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}活动任务开" in subject or "all活动任务开" in subject:
                    赛季任务 = 1
                    email_song(f'{用户邮箱}{设备号}', '执行活动任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "执行活动任务", f'{用户邮箱}', 4)

                if f"{用户邮箱}接受bug信息" in subject or "all接受bug信息" in subject:
                    是否接受bug信息用户 = 0
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[12] = f'{是否接受bug信息用户}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱}设置接受bug信息{设备号}', '接受bug信息用户', f'{报告邮箱}', 4)
                    email_song('执行操作,置接受bug信息', "接受bug信息用户", f'{用户邮箱}', 4)
                if f"{用户邮箱}不接受bug信息" in subject or "all不接受bug信息" in subject:
                    是否接受bug信息用户 = 1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[12] = f'{是否接受bug信息用户}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱}设置不接受bug信息{设备号}', '不接受bug信息用户', f'{报告邮箱}', 4)
                    email_song('执行操作,设置不接受bug信息', "不接受bug信息用户", f'{用户邮箱}', 4)
                if f"{用户邮箱}日常任务开" in subject or "all日常任务开" in subject:
                    日常任务 = 1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[14] = f'{日常任务}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱},{设备号}设置全托', "将每日执行每日任务", f'{报告邮箱}', 4)
                    email_song('设置全托', "将每日执行每日任务", f'{用户邮箱}', 4)
                else:
                    if f"{用户邮箱}日常任务关" in subject or "all日常任务关" in subject:
                        日常任务 = 0
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[14] = f'{日常任务}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}关闭全托', "停止每日执行每日任务", f'{报告邮箱}', 4)
                        email_song('关闭全托', "停止每日执行每日任务", f'{用户邮箱}', 4)
                if f"{用户邮箱}极限模式开" in subject or "all极限模式开" in subject:
                    极限模式=1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[13] = f'{极限模式}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    log(f"极限模式已修改为: {极限模式}")
                    email_song(f'{用户邮箱},{设备号}设置极限模式', "将执行极限模式", f'{报告邮箱}', 4)
                    email_song('设置极限模式', "将执行极限模式", f'{用户邮箱}', 4)
                else:
                    if f"{用户邮箱}极限模式关" in subject or "all极限模式关" in subject:
                        极限模式=0
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[13] = f'{极限模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        log(f"极限模式已修改为: {极限模式}")
                        email_song(f'{用户邮箱},{设备号}关闭极限模式', "停止极限模式", f'{报告邮箱}', 4)
                        email_song('关闭极限模式', "停止极限模式", f'{用户邮箱}', 4)
                if subject.startswith(f"{用户邮箱}宝箱"):

                    try:
                        # 提取宝箱值
                        宝箱_value_str = subject.split(f"{用户邮箱}宝箱")[1]
                        宝箱_value = int(宝箱_value_str)
                        宝箱 = min(宝箱_value, 3)  # 将宝箱值限制在3以内
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[6] = f'{箱子}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        log(f"宝箱已修改为: {宝箱}")
                        email_song(f'{用户邮箱},{设备号}宝箱设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{报告邮箱}', 4)
                        email_song('宝箱购买设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("all宝箱"):
                    try:
                        # 提取宝箱值
                        宝箱_value_str = subject.split("all宝箱")[1]
                        宝箱_value = int(宝箱_value_str)
                        宝箱 = min(宝箱_value, 3)  # 将宝箱值限制在3以内
                        log(f"宝箱已修改为: {宝箱}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[6] = f'{箱子}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}宝箱设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{报告邮箱}', 4)
                        email_song('宝箱购买设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("all单次游戏局数"):
                    try:
                        # 提取宝箱值
                        单次游戏局数_value_str = subject.split("all单次游戏局数")[1]
                        单次游戏局数 = int(单次游戏局数_value_str)
                        log(f"单次游戏局数已修改为: {单次游戏局数}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[9] = f'{单次游戏局数}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}单次游戏局数设置,批量命令',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{报告邮箱}', 4)
                        email_song('单次游戏局数设置,批量命令',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith(f"{用户邮箱}单次游戏局数"):
                    try:
                        # 提取宝箱值
                        单次游戏局数_value_str = subject.split(f"{用户邮箱}单次游戏局数")[1]
                        单次游戏局数 = int(单次游戏局数_value_str)
                        log(f"单次游戏局数已修改为: {单次游戏局数}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[9] = f'{单次游戏局数}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}单次游戏局数设置',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{报告邮箱}', 4)
                        email_song('单次游戏局数设置',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")

                if subject.startswith(f"{用户邮箱}随机战斗模式"):
                    try:
                        # 提取宝箱值
                        随机战斗模式_value_str = subject.split(f"{用户邮箱}随机战斗模式")[1]
                        随机战斗模式 = float(随机战斗模式_value_str)
                        log(f"随机战斗模式已修改为: {随机战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[10] = f'{随机战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}随机战斗模式设置',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{报告邮箱}', 4)
                        email_song('随机战斗模式设置',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("all随机战斗模式"):
                    try:
                        # 提取宝箱值
                        随机战斗模式_value_str = subject.split("all随机战斗模式")[1]
                        随机战斗模式 = float(随机战斗模式_value_str)
                        log(f"随机战斗模式已修改为: {随机战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[10] = f'{随机战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}随机战斗模式设置,批量命令',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{报告邮箱}', 4)
                        email_song('随机战斗模式设置,批量命令',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")

                if subject.startswith("all战斗模式"):
                    try:
                        # 提取宝箱值
                        战斗模式_value_str = subject.split("all战斗模式")[1]
                        战斗模式 = float(战斗模式_value_str)
                        log(f"战斗模式已修改为: {战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[11] = f'{战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)
                                if 战斗模式 == 1:
                                    战斗模式字 = "识别颜色战斗"
                                elif 战斗模式 == 2:
                                    战斗模式字 = "弱Ai识别战斗"
                                elif 战斗模式 == 3:
                                    战斗模式字 = "空战图色识别"


                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}战斗模式设置,批量命令',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{报告邮箱}', 4)
                        email_song('战斗模式设置,批量命令',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith(f"{用户邮箱}战斗模式"):
                    try:
                        # 提取宝箱值
                        战斗模式_value_str = subject.split(f"{用户邮箱}战斗模式")[1]
                        战斗模式 = float(战斗模式_value_str)
                        log(f"战斗模式已修改为: {战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[11] = f'{战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)
                                if 战斗模式 == 1:
                                    战斗模式字 = "识别颜色战斗"
                                elif 战斗模式 == 2:
                                    战斗模式字 = "弱Ai识别战斗"
                                elif 战斗模式 == 3:
                                    战斗模式字 = "空战图色识别"


                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}战斗模式设置',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{报告邮箱}', 4)
                        email_song('战斗模式设置',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if f"{用户邮箱}自动继续时间" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split(f"{用户邮箱}自动继续时间")[1]
                        自动继续时间 = int(x)  # 传递时间参数
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[8] = f'{自动继续时间}\n'
                                file.seek(0)
                                file.writelines(lines)
                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{报告邮箱}', 4)
                        email_song('设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if "all自动继续时间" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split("all自动继续时间")[1]
                        自动继续时间 = int(x)  # 传递时间参数
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[8] = f'{自动继续时间}\n'
                                file.seek(0)
                                file.writelines(lines)
                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}设置自动继续时间为',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{报告邮箱}', 4)
                        email_song('设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
            if sender_email == 用户邮箱:
                if "接受bug信息" in subject:
                    是否接受bug信息用户 = 0
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[12] = f'{是否接受bug信息用户}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱}设置接受bug信息{设备号}', '接受bug信息用户', f'{报告邮箱}', 4)
                    email_song('执行操作,置接受bug信息', "接受bug信息用户", f'{用户邮箱}', 4)
                if "不接受bug信息" in subject:
                    是否接受bug信息用户 = 1
                    file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                    try:
                        with open(file_path, "r+") as file:
                            lines = file.readlines()
                            lines[12] = f'{是否接受bug信息用户}\n'

                            file.seek(0)
                            file.writelines(lines)

                    except FileNotFoundError:
                        log(f"文件未找到: {file_path}")
                    except Exception as e:
                        log(f"发生错误: {e}")
                    email_song(f'{用户邮箱}设置不接受bug信息{设备号}', '不接受bug信息用户', f'{报告邮箱}', 4)
                    email_song('执行操作,设置不接受bug信息', "不接受bug信息用户", f'{用户邮箱}', 4)
                if subject.startswith("单次游戏局数"):
                    try:
                        # 提取宝箱值
                        单次游戏局数_value_str = subject.split("单次游戏局数")[1]
                        单次游戏局数 = int(单次游戏局数_value_str)
                        log(f"单次游戏局数已修改为: {单次游戏局数}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[9] = f'{单次游戏局数}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}单次游戏局数设置',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{报告邮箱}', 4)
                        email_song('单次游戏局数设置',
                                   f"单次游戏局数设置为{单次游戏局数}局",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("随机战斗模式"):
                    try:
                        # 提取宝箱值
                        随机战斗模式_value_str = subject.split("随机战斗模式")[1]
                        随机战斗模式 = float(随机战斗模式_value_str)
                        log(f"随机战斗模式已修改为: {随机战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[10] = f'{随机战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song(f'{用户邮箱},{设备号}随机战斗模式设置',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{报告邮箱}', 4)
                        email_song('随机战斗模式设置',
                                   f"随机战斗模式设置为{随机战斗模式}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if subject.startswith("战斗模式"):
                    try:
                        # 提取宝箱值
                        战斗模式_value_str = subject.split("战斗模式")[1]
                        战斗模式 = float(战斗模式_value_str)
                        log(f"战斗模式已修改为: {战斗模式}")
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[11] = f'{战斗模式}\n'

                                file.seek(0)
                                file.writelines(lines)
                                if 战斗模式 == 1:
                                    战斗模式字 = "识别颜色战斗"
                                elif 战斗模式 == 2:
                                    战斗模式字 = "弱Ai识别战斗"
                                elif 战斗模式 == 3:
                                    战斗模式字 = "空战图色识别"


                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}战斗模式设置',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{报告邮箱}', 4)
                        email_song('战斗模式设置,批量命令',
                                   f"战斗模式设置为 {战斗模式字}",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if "间隔时间" in subject:
                    try:
                        x = subject.split("间隔时间")[1].strip()
                        用户间隔时间 = x
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[7] = f'{用户间隔时间}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        email_song('收件间隔时间',
                                   f"收件间隔时间设置{x}局一次",
                                   f'{用户邮箱}', 4)

                    except IndexError:
                        pass
                if "自动继续时间" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split("自动继续时间")[1]
                        自动继续时间 = int(x)  # 传递时间参数
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[8] = f'{自动继续时间}\n'
                                file.seek(0)
                                file.writelines(lines)
                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")

                        email_song(f'{用户邮箱},{设备号}设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{报告邮箱}', 4)
                        email_song('设置自动继续时间',
                                   f"设置自动继续时间为 {自动继续时间} 分钟",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")
                if "停止" in subject:
                    # 提取可能存在的时间参数
                    try:
                        x = subject.split("停止")[1].strip()
                        stop_action(x)  # 传递时间参数
                    except IndexError:
                        stop_action()
                if "继续" in subject:
                    continue_action()

                if "重启" in subject:
                    stop_event.set()  # 设置停止事件，通知主线程停止
                    continue_event.clear()
                    time.sleep(60)  # 清除继续事件
                    启动()
                    stop_event.clear()  # 清除停止事件状态
                    continue_event.set()  # 设置继续事件，重新启动任务
                    email_song(f'{用户邮箱}{设备号}执行重启', '执行重启', f'{报告邮箱}', 4)
                    email_song('执行操作', "执行重启", f'{用户邮箱}', 4)

                if "赛季任务关" in subject:
                    赛季任务 = 0
                    email_song(f'{用户邮箱}停止赛季任务{设备号}', '停止赛季任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "停止赛季任务", f'{用户邮箱}', 4)
                if "赛季任务开" in subject:
                    赛季任务 = 1
                    email_song(f'{用户邮箱}{设备号}执行赛季任务', '执行赛季任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "执行赛季任务", f'{用户邮箱}', 4)
                if "活动任务关" in subject:
                    赛季任务 = 0
                    email_song(f'{用户邮箱}停止活动任务{设备号}', '停止活动任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "停止活动任务", f'{用户邮箱}', 4)
                if "活动任务开" in subject:
                    赛季任务 = 2
                    email_song(f'{用户邮箱}{设备号}执行活动任务', '执行活动任务', f'{报告邮箱}', 4)
                    email_song('执行操作', "执行活动任务", f'{用户邮箱}', 4)
                if f"日常任务开" in subject:
                    日常任务 = 1
                    email_song(f'{用户邮箱},{设备号}设置全托', "将每日执行每日任务", f'{报告邮箱}', 4)
                    email_song('设置全托', "将每日执行每日任务", f'{用户邮箱}', 4)
                else:
                    if "日常任务关" in subject:
                        日常任务 = 0
                        email_song(f'{用户邮箱},{设备号}关闭全托', "停止每日执行每日任务", f'{报告邮箱}', 4)
                        email_song('关闭全托', "停止每日执行每日任务", f'{用户邮箱}', 4)
                if subject.startswith("宝箱"):
                    try:
                        # 提取宝箱值
                        宝箱_value_str = subject.split("宝箱")[1]
                        宝箱_value = int(宝箱_value_str)
                        宝箱 = min(宝箱_value, 3)  # 将宝箱值限制在3以内
                        file_path = '/storage/emulated/0/airscript/model/战雷/参数.txt'
                        try:
                            with open(file_path, "r+") as file:
                                lines = file.readlines()
                                lines[6] = f'{箱子}\n'

                                file.seek(0)
                                file.writelines(lines)

                        except FileNotFoundError:
                            log(f"文件未找到: {file_path}")
                        except Exception as e:
                            log(f"发生错误: {e}")
                        log(f"宝箱已修改为: {宝箱}")
                        email_song(f'{用户邮箱},{设备号}宝箱设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{报告邮箱}', 4)
                        email_song('宝箱购买设置',
                                   f"宝箱设置为{宝箱},   箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开",
                                   f'{用户邮箱}', 4)
                    except ValueError:
                        log("无法解析宝箱值，忽略此命令")



            else:
                return


        def parser_email_header(msg):
            subject = msg['Subject']
            value, charset = decode_header(subject)[0]
            if charset:
                value = value.decode(charset)
            log('邮件标题： {0}'.format(value))

            hdr, addr = parseaddr(msg['From'])
            name, charset = decode_header(hdr)[0]
            if charset:
                name = name.decode(charset)
            log('发送人邮箱名称: {0}，发送人邮箱地址: {1}'.format(name, addr))

            hdr, addr = parseaddr(msg['To'])
            name, charset = decode_header(hdr)[0]
            if charset:
                name = name.decode(charset)
            log('接收人邮箱名称: {0}，接收人邮箱地址: {1}'.format(name, addr))


        def decode_str(s):
            value, charset = decode_header(s)[0]
            if charset:
                value = value.decode(charset)
            return value


        def guess_charset(msg):
            charset = msg.get_charset()
            if charset is None:
                content_type = msg.get('Content-Type', '').lower()
                for item in content_type.split(';'):
                    item = item.strip()
                    if item.startswith('charset'):
                        charset = item.split('=')[1]
                        break
            return charset


        from dateutil import parser
        from dateutil.tz import gettz


        def parse_mail_time(mail_datetime):
            formats = [
                '%a, %d %b %Y %H:%M:%S %z',
                '%a, %d %b %Y %H:%M:%S %Z',
                '%a, %d %b %Y %H:%M:%S',
                '%Y-%m-%d %H:%M:%S %z',
                '%Y-%m-%d %H:%M:%S %Z',
                '%Y-%m-%d %H:%M:%S',
            ]

            for fmt in formats:
                try:
                    dt = parser.parse(mail_datetime, yearfirst=True, dayfirst=False, fuzzy=True)
                    tz = gettz('Asia/Shanghai')
                    dt = dt.replace(tzinfo=tz)  # 如果有时区信息，就设置时区
                    return dt
                except (ValueError, OverflowError):
                    continue

            raise ValueError(f"邮件时间格式解析错误: {mail_datetime}")

if "时间":

    pause_timestamp = None


    def 加时间(x):
        global hourold, minuteold, dayold, bug数, bug时间
        bug数 += 1
        bug时间 += x
        # 创建初始时间，设置为零值，只有分钟和分钟有意义
        initial_time = datetime(2024, 1, day=dayold, hour=hourold, minute=minuteold)

        # 计算加上 x 分钟后的时间
        future_time = initial_time + timedelta(minutes=x)

        # 更新全局变量
        hourold = future_time.hour
        minuteold = future_time.minute
        dayold = future_time.day


    def 记录暂停时间(x):
        global pause_timestamp,是否强行登录
        wait_time = 1
        if x is not None:
            try:
                wait_time = int(x)
                if wait_time < 1:
                    wait_time = 1  # 最小等待时间为1小时
            except ValueError:
                wait_time = 1
        now = datetime.now()  # 获取当前时间
        pause_timestamp = now.timestamp()
        log(f"记录暂停时间: {now}")
        if 是否强行登录==0:
            email_song(f'{用户邮箱}停止了程序执行{设备号}',
                       f'开始时间{dayold} 日 {hourold} 小时, {minuteold} 分钟,记录暂停时间: {now},将在{wait_time}分钟后自动继续,也可以直接发邮件命令进行继续执行',
                       f'{报告邮箱}', 4)
            email_song('停止了程序执行',
                       f'开始时间{dayold} 日 {hourold} 小时, {minuteold} 分钟,记录暂停时间: {now},将在{wait_time}分钟后自动继续,也可以直接发邮件命令进行继续执行',
                       f'{用户邮箱}', 4)
        else:
            email_song(f'{用户邮箱}停止了程序执行{设备号},将在{wait_time}分钟后自动继续',
                       f'开始时间{dayold} 日 {hourold} 小时, {minuteold} 分钟,记录暂停时间: {now},将在{wait_time}分钟后自动继续,也可以直接发邮件命令进行继续执行',
                       f'{报告邮箱}', 4)
            email_song(f'抢登成功,停止了程序执行,将在{wait_time}分钟后自动继续',
                       f'开始时间{dayold} 日 {hourold} 小时, {minuteold} 分钟,记录暂停时间: {now},将在{wait_time}分钟后自动继续,也可以直接发邮件命令进行继续执行',
                       f'{用户邮箱}', 4)
            是否强行登录=0



    def 记录暂停():
        global pause_timestamp
        now = datetime.now()  # 获取当前时间
        pause_timestamp = now.timestamp()
        log(f"记录暂停时间: {now}")


    def 计算并更新():

        global pause_timestamp, hourold, minuteold, dayold, 总暂停小时, 总暂停分钟, 总暂停天, 总暂停时长, 总消耗时长小时, 总消耗时长分钟
        time.sleep(5)

        if pause_timestamp is None:
            log("没有暂停时间记录，无法计算时间差。")
            return

        now = datetime.now()  # 获取当前时间
        current_timestamp = now.timestamp()
        时间差 = current_timestamp - pause_timestamp

        # 计算增加的小时、分钟和天数
        hours = int(时间差 // 3600)
        minutes = int((时间差 % 3600) // 60)
        days = int(hours // 24)
        hours = hours % 24

        # 更新旧的时间变量
        dayold += days
        hourold += hours
        minuteold += minutes

        # 处理分钟或小时超出正常范围的情况
        hourold += minuteold // 60
        minuteold = minuteold % 60
        dayold += hourold // 24
        hourold = hourold % 24


    def 计算并更新时间():

        global pause_timestamp, hourold, minuteold, dayold, 总暂停小时, 总暂停分钟, 总暂停天, 总暂停时长, 总消耗时长小时, 总消耗时长分钟
        time.sleep(5)

        if pause_timestamp is None:
            log("没有暂停时间记录，无法计算时间差。")
            return

        now = datetime.now()  # 获取当前时间
        current_timestamp = now.timestamp()
        时间差 = current_timestamp - pause_timestamp

        # 计算增加的小时、分钟和天数
        hours = int(时间差 // 3600)
        minutes = int((时间差 % 3600) // 60)
        days = int(hours // 24)
        hours = hours % 24

        # 更新旧的时间变量
        dayold += days
        hourold += hours
        minuteold += minutes

        # 处理分钟或小时超出正常范围的情况
        hourold += minuteold // 60
        minuteold = minuteold % 60
        dayold += hourold // 24
        hourold = hourold % 24

        # 计算总暂停时长的小时、分钟和天数
        暂停小时 = hours

        暂停分钟 = minutes
        # 暂停时长 = 暂停天 * 0.2
        # 计算总暂停时长的小时、分钟和天数
        总暂停分钟 += 暂停分钟
        总暂停小时 += 暂停小时 + 总暂停分钟 // 60
        总暂停分钟 = 总暂停分钟 % 60
        消耗时长小时 = 暂停小时 * 0.2
        消耗时长分钟 = 暂停分钟 * 0.2 + (消耗时长小时 % 1) * 60
        消耗时长小时 = 消耗时长小时 // 1
        消耗时长小时 += 消耗时长分钟 // 60
        消耗时长分钟 = 消耗时长分钟 % 60

        总消耗时长分钟 = 总消耗时长分钟 + 消耗时长分钟
        总消耗时长小时 = 总消耗时长小时 + 消耗时长小时 + 总消耗时长分钟 // 60
        总消耗时长分钟 = 总消耗时长分钟 % 60 + (总消耗时长小时 % 1) * 60
        总消耗时长小时 = 总消耗时长小时 // 1 + 总消耗时长分钟 // 60
        总消耗时长分钟 = 总消耗时长分钟 % 60

        log(f"更新后的时间: {dayold} 天, {hourold} 小时, {minuteold} 分钟")

        email_song(f'继续程序执行{用户邮箱}{设备号}',
                   f'消耗时长{消耗时长小时}小时,{消耗时长分钟}分钟 ,更新后的时间: {dayold} 天, {hourold} 小时, {minuteold} 分钟\n暂停时长:{暂停小时} 小时, {暂停分钟} 分钟\n总消耗时长: {总消耗时长小时} 小时, {总消耗时长分钟} 分钟.',
                   f'{报告邮箱}', 4)
        email_song('继续程序执行',
                   f'消耗时长{消耗时长小时}小时,{消耗时长分钟}分钟,更新后的时间: {dayold} 天, {hourold} 小时, {minuteold} 分钟\n暂停时长:{暂停小时} 小时, {暂停分钟} 分钟\n总消耗时长: {总消耗时长小时} 小时, {总消耗时长分钟} 分钟.',
                   f'{用户邮箱}', 4)
        pause_timestamp = None


    def oldtime(hour, minute=999, day=999, second=999):
        # 获取当前的年份和月份
        now = datetime.now()
        year = now.year
        month = now.month
        if minute == 999:
            minute = now.minute
        if second == 999:
            second = now.second
        if day == 999:
            day = now.day
        # 检查月份和日期是否合理
        if month < 1 or month > 12:
            log("月份输入错误！")
            return None
        if day < 1 or day > 31:
            log("日期输入错误！")
            return None

        # 根据月份调整日期范围
        if month in [4, 6, 9, 11]:
            if day > 30:
                log("日期输入错误！")
                return None
        elif month == 2:
            if year % 4 == 0:
                if day > 29:
                    log("日期输入错误！")
                    return None
            else:
                if day > 28:
                    log("日期输入错误！")
                    return None

        # 如果日期不合理，调整日期
        if day > 28:
            if month == 2 and day > 29:
                month += 1
                day = 1
            elif month in [4, 6, 9, 11] and day > 30:
                month += 1
                day = 1
            elif month == 12 and day > 31:
                year += 1
                month = 1
                day = 1
        # 创建 datetime 对象
        dt = datetime(year, month, day, hour, minute, second)

        # 获取时间戳
        timestamp = dt.timestamp()

        return timestamp


    def nowtime(小时=999, 分钟=999, 天=999):
        global timenow
        global hour, minute, second, day
        global hours, minutes, secs, whole_seconds

        # 获取当前时间

        now = datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second
        day = now.day
        # 如果有小时、分钟或天的增量
        if 小时 != 999 or 分钟 != 999 or 天 != 999:
            时间差 = time.time() - oldtime(小时, 分钟, 天)
            whole_seconds = int(时间差)
            fractional_seconds = 时间差 - whole_seconds

            # 计算小时、分钟和秒
            hours = whole_seconds // 3600
            minutes = (whole_seconds % 3600) // 60
            secs = whole_seconds % 60

            # 将小数部分添加到秒数中
            secs += fractional_seconds
            log(f"{hours}小时 {minutes}分钟 {secs:.1f}秒")

            return 时间差
if "必须操作":
    #
    # def 加速器():
    #     Intent.run("com.etalien.booster")
    #
    #
    #
    #
    # 加速器()
    # time.sleep(4)
    # log("停止")
    # time.sleep(3)
    def tu(图片, 点0=1, 文字1=1, 图1=1, 左上宽=0, 左上高=0, 右下高=xk, 右下宽=xg, 灰度0RGB1=0, 准确度=0.80, 输出=0):
        try:
            xxxx = 图片
            if xxxx == "XX":
                输出 = 1
            time.sleep(0.5)
            global buzsk, buzsg, buyxk, buyxg
            # 用法cao_tu(第一个图片名，是否点击1为否0为是，第二个图片，左上宽，左上高，右下宽，右下高)
            #
            #
            if 右下宽 == 1 or 右下高 == 1:
                右下宽 = xk
                右下高 = xg
            if 设备 == 1:
                if 灰度0RGB1 == 0:
                    res = FindImages.find_template([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                   confidence=准确度)
                    if FindImages.find_template([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                confidence=准确度):
                        if True:
                            if xxxx == "2":
                                log("找到了退出")
                            else:
                                log("找到", xxxx)
                    else:
                        if 输出 == 0:
                            if xxxx != "2":
                                log(f"未找到图片{xxxx}")

                        return False
                else:
                    res = FindImages.find_template([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                   confidence=准确度, rgb=True)
                    if FindImages.find_template([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                confidence=准确度, rgb=True):
                        if True:
                            if xxxx == "2":
                                log("找到了退出")
                            else:
                                log("找到", xxxx)
                    else:
                        if 输出 == 0:
                            if xxxx != "2":
                                log(f"未找到图片{xxxx}")

                        return False
            else:
                if 灰度0RGB1 == 0:
                    res = FindImages.find([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                          confidence=准确度)
                    if FindImages.find([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                       confidence=准确度):
                        if True:
                            if xxxx == "2":
                                log("找到了退出")
                            else:
                                log("找到", xxxx)
                    else:
                        if 输出 == 0:
                            if xxxx != "2":
                                log(f"未找到图片{xxxx}")

                        return False
                else:
                    res = FindImages.find_template([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                   confidence=准确度, rgb=True)
                    if FindImages.find_template([R.img(f"{xxxx}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                confidence=准确度, rgb=True):
                        if True:
                            if xxxx == "2":
                                log("找到了退出")
                            else:
                                log("找到", xxxx)
                    else:
                        if 输出 == 0:
                            if xxxx != "2":
                                log(f"未找到图片{xxxx}")

                        return False

            if res:
                # 提取坐标
                buzsk = res["rect"][0]
                buzsg = res["rect"][1]
                buyxk = res["rect"][2]
                buyxg = res["rect"][3]

                if 点0 == 0:
                    if True:
                        if xxxx == "2":
                            log("点击了退出")
                        else:
                            log("点击了", xxxx)

                    # 点击中心坐标
                    click(res["center_x"], res["center_y"])
                if 文字1 != 1:
                    zi(文字1, 0, buzsk, buzsg, buyxk, buyxg)
                if 图1 != 1:
                    xxz2 = 图1
                    if 灰度0RGB1 == 0:

                        res = FindImages.find_template([R.img(f"{xxz2}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                       confidence=准确度)
                    else:
                        res = FindImages.find_template([R.img(f"{xxz2}.png"), ], rect=[左上宽, 左上高, 右下高, 右下宽],
                                                       confidence=准确度, rgb=True)
                    if res2:
                        if 输出 == 0:
                            log("在第一个图片的范围内找到第二个图片")
                        time.sleep(1)
                        click(res["center_x"], res["center_y"])
                    else:

                        if 输出 == 0:
                            log("在第一个图片的范围内未找到第二个图片")
                        return False
            else:
                log(f"未找到图片{xxxx}")

                return False
            return True and 666
        except Exception as e:
            log(f"发生错误: {e}")
            email_song(f'图片{设备号}', f' {图片}, {点0}{文字1}, {图1}, {左上宽}, {左上高}, {右下高}, {右下宽}, {灰度0RGB1}, {准确度}, {输出}\n{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}')
            错误()



    def zi(字, 点击0=0, x=0, y=0, x1=xk, y1=xg, 输出=0):
        try:
            time.sleep(0.5)
            res = Ocr.mlkitocr_v2(rect=[x, y, x1, y1], pattern=f'.*{字}.*')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    if 点击0 == 0:
                        if 点击0 == 0:
                            click(r.center_x, r.center_y)
                            log(f"点击’{字}‘成功")
                            return True
                        else:
                            if 输出 == 0:
                                log(f"点击’{字}‘未成功")

                            return False
                    return True

            else:
                if 输出 == 0:
                    log(f"未找到’{字}‘")
                return False
        except Exception as e:
            log(f"发生错误: {e}")
            email_song(f'字{设备号}', f'{字}{点击}{x} {y} {x1} {y1}{输出} \n {e}{e.__traceback__.tb_lineno}', f'{报告邮箱}')
            错误()

    def 模型(模型名, 是否输出坐标1=1, x=0, y=0, xz=0, yz=0):
        global 识别x, 识别y,kekai
        if 游戏结束 == 1:
            return False
        if True:
            mengzhi = 1
            if 模型名 == "敌船":
                if not FindColors.find("746,518,#241F23|751,521,#DDDDDF|755,521,#FFFFFF|757,521,#FFFFFF|742,521,#D2D2D4",
                                   rect=[724, 428, 787, 575]):
                    开镜(1, 0)
                time.sleep(1)
                mengzhi=0

            if x == 0:
                ts = yolo.find_all()
            else:
                ts = yolo.find_all(rect=[x, y, xz, yz])

            while True:
                for r in ts:
                    # log(r.label)  # 目标名称
                    # log(r.prob)  # 可信度
                    # log(r.x)  # 坐标x
                    # log(r.y)  # 坐标y
                    # log(r.w)  # 目标宽度
                    # log(r.h)  # 目标高度
                    if 模型名 == r.label:
                        # log(r.label)  # 目标名称
                        # log(r.prob)  # 可信度
                        # log(r.x)  # 坐标x
                        # log(r.y)  # 坐标y
                        # log(r.w)  # 目标宽度
                        # log(r.h)  # 目标高度
                        log("成功找到", r.label)
                        if 模型名=="在目标附近":
                            if not FindColors.find("662,190,#FF6D66", rect=[131, 21, 1203, 599], diff=0.90):
                                return False
                        if 是否输出坐标1 == 1:

                            return True
                        else:
                            if mengzhi == 0:
                                kekai = 0
                            else:
                                kekai = 1
                            识别x = r.x
                            识别y = r.y
                            # if 模型名 == "敌船":
                            #     识别y -= 10
                            # log(识别x//1,识别y//1)
                            return True

                else:
                    return False

if "特殊函数":
    def 海载具():

        挑选 = random.random()
        if 挑选 > 0.66:
            # 紫色
            point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
            if point:
                # 打印 x坐标 和 y坐标
                click(point.x, point.y)
            else:
                if random.random() >= 0.5:
                    # 金色
                    point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("851,523,#282729|823,509,#313235|842,504,#343639",
                                                rect=[92, 130, 1161, 670])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
                else:
                    point = FindColors.find("851,523,#282729|823,509,#313235|842,504,#343639",
                                            rect=[92, 130, 1161, 670])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
        elif 0.66 >= 挑选 > 0.33:
            # 金色
            point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
            if point:
                # 打印 x坐标 和 y坐标
                click(point.x, point.y)
            else:
                if random.random() >= 0.5:
                    point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("851,523,#282729|823,509,#313235|842,504,#343639",
                                                rect=[92, 130, 1161, 670])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
                else:
                    point = FindColors.find("851,523,#282729|823,509,#313235|842,504,#343639",
                                            rect=[92, 130, 1161, 670])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
        else:
            point = FindColors.find("851,523,#282729|823,509,#313235|842,504,#343639",
                                    rect=[92, 130, 1161, 670])
            if point:
                # 打印 x坐标 和 y坐标
                click(point.x, point.y)
            else:
                if random.random() >= 0.5:
                    point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
                else:
                    point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)

    def 空载具():

        挑选 = random.random()
        if 挑选 > 0.66:
            # 紫色
            point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
            if point:
                # 打印 x坐标 和 y坐标
                click(point.x, point.y)
            else:
                if random.random() >= 0.5:
                    # 金色
                    point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("406,270,#F7F5F4|406,263,#2C2D2E",
                                                rect=[92, 130, 1161, 670])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
                else:
                    point = FindColors.find("406,270,#F7F5F4|406,263,#2C2D2E",
                                            rect=[92, 130, 1161, 670])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
        elif 0.66 >= 挑选 > 0.33:
            # 金色
            point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
            if point:
                # 打印 x坐标 和 y坐标
                click(point.x, point.y)
            else:
                if random.random() >= 0.5:
                    point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("406,270,#F7F5F4|406,263,#2C2D2E",
                                                rect=[92, 130, 1161, 670])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
                else:
                    point = FindColors.find("406,270,#F7F5F4|406,263,#2C2D2E",
                                            rect=[92, 130, 1161, 670])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
        else:
            point = FindColors.find("406,270,#F7F5F4|406,263,#2C2D2E",
                                    rect=[92, 130, 1161, 670])
            if point:
                # 打印 x坐标 和 y坐标
                click(point.x, point.y)
            else:
                if random.random() >= 0.5:
                    point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)
                else:
                    point = FindColors.find("348,281,#5C2C91", rect=[115, 126, 1219, 692])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    else:
                        point = FindColors.find("605,269,#C89123", rect=[115, 126, 1219, 692])
                        if point:
                            # 打印 x坐标 和 y坐标
                            click(point.x, point.y)

    def 切空():
        global 海1空2, 现次数
        if stop_event.is_set():
            return
        if 加入战斗():
            time.sleep(2)
        else:
            zi("取消", 0, 322, 439, 563, 549)
            time.sleep(2)
            if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern='稍后'):
                time.sleep(4)
                click(815, 649)
                time.sleep(3)
                退出()
                time.sleep(3)
            退出()
        time.sleep(1)
        click(137, 637)
        time.sleep(1)
        click(98, 557)
        time.sleep(1)
        res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
        if res:
            # 循环打印识别到的每一个段落
            for r in res:
                click(r.center_x, r.center_y)
        else:
            退出()
            time.sleep(1)
            click(137, 637)
            time.sleep(1)
            click(98, 557)
            time.sleep(1)
            res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
        time.sleep(1)
        click(197, 318)
        time.sleep(1)
        click(291, 313)
        time.sleep(1)
        click(379, 316)
        time.sleep(1)
        click(469, 310)
        time.sleep(1)
        click(167, 414)
        time.sleep(1)
        click(796, 167)
        time.sleep(1)
        if random.random() < 0.5:
            # 左滑
            action.slide(672, 392, 1148, 392, 700)
        else:
            # 右滑
            action.slide(672, 392, 233, 414, 700)
        time.sleep(1)
        挑选 = random.random()
        if 挑选 > 0.66:
            # 美国
            click(98, 140)
        elif 0.66 >= 挑选 > 0.33:
            # 德国
            click(109, 261)
        else:
            # sul
            click(98, 368)
        time.sleep(1)
        time.sleep(1)
        空载具()
        time.sleep(1)
        if not zi("安装", 0, 885, 605, 1135, 692, 1):
            挑选 = random.random()
            if 挑选 > 0.66:
                # 美国
                click(98, 140)
            elif 0.66 >= 挑选 > 0.33:
                # 德国
                click(109, 261)
            else:
                # sul
                click(98, 368)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            空载具()

            time.sleep(1)
            zi("安装", 0, 885, 605, 1135, 692, 1)
        time.sleep(1)
        click(145, 637)
        time.sleep(1)
        退出()
    def 切海():
        click(98, 577)
        time.sleep(2)
        res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
        if res:
            # 循环打印识别到的每一个段落
            for r in res:
                click(r.center_x, r.center_y)
        else:
            退出()
            time.sleep(1)
            click(98, 577)
            res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
        time.sleep(1)
        click(417, 412)
        time.sleep(0.5)
        click(335, 329)
        time.sleep(0.5)
        click(425, 313)
        time.sleep(1)
        click(936, 162)
        time.sleep(1)
        if random.random() < 0.5:
            # 左滑
            action.slide(672, 392, 1148, 392, 700)
        else:
            # 右滑
            action.slide(672, 392, 233, 414, 700)
        time.sleep(1)
        海载具()
        time.sleep(1)
        if not zi("中", 0, 885, 605, 1135, 692, 1):
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            海载具()
            time.sleep(1)
            zi("中", 0, 885, 605, 1135, 692, 1)

        退出()
        time.sleep(1)

    def 随机切换载具():
        global 海1空2, 现次数
        if stop_event.is_set():
            return
        if 加入战斗():
            time.sleep(2)
        else:
            zi("取消", 0, 322, 439, 563, 549)
            time.sleep(2)
            if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern='稍后'):
                time.sleep(4)
                click(815, 649)
                time.sleep(3)
                退出()
                time.sleep(3)
            退出()
        if 海1空2 == 1:
            click(98, 577)
            time.sleep(2)
            res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
            else:
                退出()
                time.sleep(1)
                click(98, 577)
                res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        click(r.center_x, r.center_y)
            time.sleep(1)
            click(417, 412)
            time.sleep(0.5)
            click(335, 329)
            time.sleep(0.5)
            click(425, 313)
            time.sleep(1)
            click(936, 162)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            海载具()
            time.sleep(1)
            if not zi("中", 0, 885, 605, 1135, 692, 1):
                if random.random() < 0.5:
                    # 左滑
                    action.slide(672, 392, 1148, 392, 700)
                else:
                    # 右滑
                    action.slide(672, 392, 233, 414, 700)
                time.sleep(1)
                海载具()
                time.sleep(1)
                zi("中", 0, 885, 605, 1135, 692, 1)

            退出()
            time.sleep(1)
            切换模式(3)
            time.sleep(1)
            click(137, 637)
            time.sleep(1)
            click(98, 557)
            time.sleep(1)
            res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
            else:
                退出()
                time.sleep(1)
                click(137, 637)
                time.sleep(1)
                click(98, 557)
                time.sleep(1)
                res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        click(r.center_x, r.center_y)
            time.sleep(1)
            click(197, 318)
            time.sleep(1)
            click(291, 313)
            time.sleep(1)
            click(379, 316)
            time.sleep(1)
            click(469, 310)
            time.sleep(1)
            click(167, 414)
            time.sleep(1)
            click(796, 167)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            挑选 = random.random()
            if 挑选 > 0.66:
                # 美国
                click(98, 140)
            elif 0.66 >= 挑选 > 0.33:
                # 德国
                click(109, 261)
            else:
                # sul
                click(98, 368)
            time.sleep(1)
            time.sleep(1)
            空载具()
            time.sleep(1)
            if not zi("安装", 0, 885, 605, 1135, 692, 1):
                挑选 = random.random()
                if 挑选 > 0.66:
                    # 美国
                    click(98, 140)
                elif 0.66 >= 挑选 > 0.33:
                    # 德国
                    click(109, 261)
                else:
                    # sul
                    click(98, 368)
                time.sleep(1)
                if random.random() < 0.5:
                    # 左滑
                    action.slide(672, 392, 1148, 392, 700)
                else:
                    # 右滑
                    action.slide(672, 392, 233, 414, 700)
                time.sleep(1)
                空载具()
                time.sleep(1)
                zi("安装", 0, 885, 605, 1135, 692, 1)
            time.sleep(1)
            click(145, 637)
            time.sleep(1)
            退出()

        elif 海1空2 == 2:
            time.sleep(1)
            click(137, 637)
            time.sleep(1)
            click(98, 557)
            time.sleep(1)
            res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
            else:
                退出()
                time.sleep(1)
                click(137, 637)
                time.sleep(1)
                click(98, 557)
                time.sleep(1)
                res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        click(r.center_x, r.center_y)
            time.sleep(1)
            click(197, 318)
            time.sleep(1)
            click(291, 313)
            time.sleep(1)
            click(379, 316)
            time.sleep(1)
            click(469, 310)
            time.sleep(1)
            click(167, 414)
            time.sleep(1)
            click(796, 167)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            挑选 = random.random()
            if 挑选 > 0.66:
                # 美国
                click(98, 140)
            elif 0.66 >= 挑选 > 0.33:
                # 德国
                click(109, 261)
            else:
                # sul
                click(98, 368)
            time.sleep(1)
            time.sleep(1)
            空载具()
            time.sleep(1)
            if not zi("安装", 0, 885, 605, 1135, 692, 1):
                挑选 = random.random()
                if 挑选 > 0.66:
                    # 美国
                    click(98, 140)
                elif 0.66 >= 挑选 > 0.33:
                    # 德国
                    click(109, 261)
                else:
                    # sul
                    click(98, 368)
                time.sleep(1)
                if random.random() < 0.5:
                    # 左滑
                    action.slide(672, 392, 1148, 392, 700)
                else:
                    # 右滑
                    action.slide(672, 392, 233, 414, 700)
                time.sleep(1)
                空载具()

                time.sleep(1)
                zi("安装", 0, 885, 605, 1135, 692, 1)
            time.sleep(1)
            click(145, 637)
            time.sleep(1)
            退出()
            切换模式(1)
            time.sleep(1)
            退出()
            click(98, 577)
            time.sleep(2)
            res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
            else:
                退出()
                time.sleep(1)
                click(98, 577)
                res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        click(r.center_x, r.center_y)
            time.sleep(1)
            click(417, 412)
            time.sleep(0.5)
            click(335, 329)
            time.sleep(0.5)
            click(425, 313)
            time.sleep(1)
            click(936, 162)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            海载具()
            time.sleep(1)
            if not zi("中", 0, 885, 605, 1135, 692, 1):
                if random.random() < 0.5:
                    # 左滑
                    action.slide(672, 392, 1148, 392, 700)
                else:
                    # 右滑
                    action.slide(672, 392, 233, 414, 700)
                time.sleep(1)
                海载具()
                time.sleep(1)
                zi("中", 0, 885, 605, 1135, 692, 1)

            退出()
            time.sleep(1)
        else:
            切换模式(3)
            time.sleep(1)
            退出()
            time.sleep(1)
            click(137, 637)
            time.sleep(1)
            click(98, 557)
            time.sleep(1)
            res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
            else:
                退出()
                time.sleep(1)
                click(137, 637)
                time.sleep(1)
                click(98, 557)
                time.sleep(1)
                res = Ocr.mlkitocr_v2(rect=[189, 10, 464, 93], pattern='件')
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        click(r.center_x, r.center_y)
            time.sleep(1)
            click(197, 318)
            time.sleep(1)
            click(291, 313)
            time.sleep(1)
            click(379, 316)
            time.sleep(1)
            click(469, 310)
            time.sleep(1)
            click(167, 414)
            time.sleep(1)
            click(796, 167)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            挑选 = random.random()
            if 挑选 > 0.66:
                # 美国
                click(98, 140)
            elif 0.66 >= 挑选 > 0.33:
                # 德国
                click(109, 261)
            else:
                # sul
                click(98, 368)
            time.sleep(1)
            time.sleep(1)
            空载具()
            time.sleep(1)
            if not zi("安装", 0, 885, 605, 1135, 692, 1):
                挑选 = random.random()
                if 挑选 > 0.66:
                    # 美国
                    click(98, 140)
                elif 0.66 >= 挑选 > 0.33:
                    # 德国
                    click(109, 261)
                else:
                    # sul
                    click(98, 368)
                time.sleep(1)
                if random.random() < 0.5:
                    # 左滑
                    action.slide(672, 392, 1148, 392, 700)
                else:
                    # 右滑
                    action.slide(672, 392, 233, 414, 700)
                time.sleep(1)
                空载具()
                time.sleep(1)
                zi("安装", 0, 885, 605, 1135, 692, 1)
            time.sleep(1)
            click(145, 637)
            time.sleep(1)
            退出()
            切换模式(1)
            time.sleep(1)
            退出()
            click(98, 577)
            time.sleep(2)
            res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
            if res:
                # 循环打印识别到的每一个段落
                for r in res:
                    click(r.center_x, r.center_y)
            else:
                退出()
                time.sleep(1)
                click(98, 577)
                res = Ocr.mlkitocr_v2(rect=[499, 19, 708, 90], pattern='件')
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        click(r.center_x, r.center_y)
            time.sleep(1)
            click(417, 412)
            time.sleep(0.5)
            click(335, 329)
            time.sleep(0.5)
            click(425, 313)
            time.sleep(1)
            click(936, 162)
            time.sleep(1)
            if random.random() < 0.5:
                # 左滑
                action.slide(672, 392, 1148, 392, 700)
            else:
                # 右滑
                action.slide(672, 392, 233, 414, 700)
            time.sleep(1)
            海载具()
            time.sleep(1)
            if not zi("中", 0, 885, 605, 1135, 692, 1):
                if random.random() < 0.5:
                    # 左滑
                    action.slide(672, 392, 1148, 392, 700)
                else:
                    # 右滑
                    action.slide(672, 392, 233, 414, 700)
                time.sleep(1)
                海载具()
                time.sleep(1)
                zi("中", 0, 885, 605, 1135, 692, 1)

            退出()
            time.sleep(1)
    if "抽奖判断":
        def process_gold():
            if FindColors.find(
                    "623,365,#97711B|616,362,#CCA654|608,336,#B07509|655,197,#E0E0E0|510,188,#4D88A4|735,192,#4D88A4",
                    rect=[359, 133, 936, 596], diff=0.90):
                time.sleep(1)
                global jinbici, jinbi, chi, jinbi5, jinbi7, jinbi15, cuowuci
                jinbici += 1
                res = Ocr.mlkitocr_v2(rect=[523, 432, 770, 489])
                if res:
                    for r in res:
                        text = r.text
                        if text == "乙":
                            text = "2"
                        log("获得金币", text)
                        try:
                            jinbiold = jinbi
                            chi += 1
                            jinbi = jinbi + int(text.replace(',', ''))
                            if int(text.replace(',', '')) == 5:
                                jinbi5 += 1
                            elif int(text.replace(',', '')) == 7:
                                jinbi7 += 1
                            elif int(text.replace(',', '')) == 15:
                                jinbi15 += 1
                            else:
                                jinbicha = jinbi - jinbi5 * 5 - jinbi7 * 7 - jinbi15 * 15
                                if jinbicha == 5:
                                    jinbi5 += 1
                                elif jinbicha == 7:
                                    jinbi7 += 1
                                elif jinbicha == 15:
                                    jinbi15 += 1
                        except ValueError as e:
                            cuowuci += 1
                            log(f"Error converting '{text}' to int: {e}")
            else:
                log("未找到金币")
                time.sleep(1)


        # 定义处理灭火器的函数
        def process_fire_extinguisher():
            if FindColors.find(
                    "653,346,#D54936|713,215,#4D88A4|524,204,#4D88A4|614,346,#2E3336|659,325,#FDE5DF|660,307,#E1E3E8",
                    rect=[359, 133, 936, 596], diff=0.98) or tu("3", 1, 1, 1, 465, 234, 813, 490, 1, 0.8):
                time.sleep(1)
                global miaohuoci, miaohuo, chi, cuowuci
                miaohuoci += 1
                res = Ocr.mlkitocr_v2(rect=[523, 432, 770, 489])
                if res:
                    for r in res:
                        text = r.text
                        if text == "乙":
                            text = "2"
                        log("灭火器", text)
                        try:
                            chi += 1
                            miaohuo = miaohuo + int(text.replace(',', ''))
                        except ValueError as e:
                            cuowuci += 1
                            log(f"Error converting '{text}' to int: {e}")
            else:
                log("未找到灭火器")
                time.sleep(1)


        # 定义处理烟雾的函数

        def process_smoke():
            if FindColors.find(
                    "615,379,#4C4435|642,332,#E6E7E9|623,328,#DDE1E4|741,178,#4D88A4|528,193,#4D88A4|623,328,#DDE1E4",
                    rect=[395, 139, 831, 548]):
                time.sleep(1)
                global yanwuci, yanwu, chi, cuowuci
                yanwuci += 1
                res = Ocr.mlkitocr_v2(rect=[523, 432, 770, 489])
                if res:
                    for r in res:
                        text = r.text
                        if text == "乙":
                            text = "2"
                        log("获得烟雾", text)
                        try:
                            chi += 1
                            yanwu = yanwu + int(text.replace(',', ''))
                        except ValueError as e:
                            cuowuci += 1
                            log(f"Error converting '{text}' to int: {e}")
            else:
                log("未找到烟雾")
                time.sleep(1)


        # 定义处理银币的函数
        def process_silver_coin():
            if FindColors.find(
                    "613,349,#C3CDD6|676,199,#4D88A4|682,208,#4D88A4|670,385,#848484|635,363,#606368",
                    rect=[420, 139, 915, 498], diff=0.90) and tu("银币", 1, 1, 1, 465, 234, 813, 490, 1, 0.8):
                time.sleep(1)
                global yinbici, yinbi, chi, yingbi1000, yingbi1500, yingbi3000, cuowuci
                yinbici += 1
                res = Ocr.mlkitocr_v2(rect=[471, 439, 839, 486])
                if res:
                    for r in res:
                        text = r.text
                        if text == "乙":
                            text = "2"
                        log("获得银币", text)
                        try:
                            chi += 1
                            yinbiold = yinbi
                            yinbi = yinbi + int(text.replace(',', ''))
                            if int(text.replace(',', '')) == 1000:
                                yingbi1000 += 1
                            elif int(text.replace(',', '')) == 1500:
                                yingbi1500 += 1
                            elif int(text.replace(',', '')) == 3000:
                                yingbi3000 += 1
                            else:
                                yingbicha = yinbi - yingbi3000 * 3000 - yingbi1500 * 1500 - yingbi1000 * 1000
                                if yingbicha == 1000:
                                    yingbi1000 += 1
                                elif yingbicha == 1500:
                                    yingbi1500 += 1
                                elif yingbicha == 3000:
                                    yingbi3000 += 1
                        except ValueError as e:
                            cuowuci += 1
                            log(f"Error converting '{text}' to int: {e}")
            else:
                log("未找到银币")
                time.sleep(1)


        # 定义处理季票的函数
        def process_ticket():
            # if FindColors.find(
            #         "644,326,#F5C9C9|591,356,#DE3A39|712,202,#4D88A4|539,204,#4D88A4|627,383,#DB2B2C",
            #         rect=[455, 170, 837, 480]):
            if tu("票", 1, 1, 1, 455, 170, 837, 480, 0, 0.8):

                time.sleep(1)
                global piaoci, piao, chi, piao10, piao20, piao100, cuowuci
                piaoci += 1
                res = Ocr.mlkitocr_v2(rect=[523, 432, 770, 489])
                if res:
                    for r in res:
                        text = r.text
                        if text == "乙":
                            text = "2"
                        log("获得季票", text)
                        try:
                            chi += 1
                            piaoold = piao
                            piao = piao + int(text.replace(',', ''))
                            if int(text.replace(',', '')) == 10:
                                piao10 += 1
                            elif int(text.replace(',', '')) == 20:
                                piao20 += 1
                            elif int(text.replace(',', '')) == 100:
                                piao100 += 1
                            else:
                                piaocha = piao - piao10 * 10 - piao20 * 20 - piao100 * 100
                                if piaocha == 10:
                                    piao10 += 1
                                elif piaocha == 20:
                                    piao20 += 1
                                elif piaocha == 100:
                                    piao100 += 1
                        except ValueError as e:
                            cuowuci += 1
                            log(f"Error converting '{text}' to int: {e}")
            else:
                log("未找到季票")
                time.sleep(1)


        # 定义处理修理包的函数
        def process_repair_kit():
            if FindColors.find(
                    "543,199,#4D88A4|627,383,#7A634B|654,379,#7D644C|706,185,#4D88A4|757,203,#4D88A4",
                    rect=[347, 123, 926, 574], diff=0.90):
                time.sleep(1)
                global xiulici, xiuli, chi, cuowuci
                xiulici += 1
                res = Ocr.mlkitocr_v2(rect=[523, 432, 770, 489])
                if res:
                    for r in res:
                        text = r.text
                        if text == "乙":
                            text = "2"
                        log("获得修理包", text)
                        try:
                            chi += 1
                            xiuli = xiuli + int(text.replace(',', ''))
                        except ValueError as e:
                            cuowuci += 1
                            log(f"Error converting '{text}' to int: {e}")
            else:
                log("未找到修理包")
                time.sleep(1)


        # 定义处理未知物品的函数
        def process_unknown_item():
            global qitaci, chi, qita, qitacu, cuowuci
            if FindImages.find_all_template([R.img("海战修理包.png"), ], rect=[450, 229, 807, 442], confidence=0.80,
                                            rgb=True):
                res = Ocr.mlkitocr_v2(rect=[523, 432, 770, 489])
                if res:
                    # 循环打印识别到的每一个段落
                    for r in res:
                        text = r.text
                        qitaci += 1

                        # 如果识别到"乙"，替换成"2"
                        if text == "乙":
                            text = "2"

                        log("海战修理包", text)  # 打印替换后的文本
                        try:
                            chi += 1
                            qita = qita + int(text.replace(',', ''))
                        except ValueError as e:
                            log(f"Error converting '{a}' to int: {e}")
                            cuowuci += 1
                else:
                    log("海战修理包")
    if "计算几率":
        def cumulative_distribution_function(x):
            """
            计算标准正态分布的累计分布函数
            """
            return 0.5 * (1 + math.erf(x / math.sqrt(2)))


        def 移除(percentage_string):
            try:
                # 移除百分号
                percentage_string_without_percent = percentage_string.replace("%", "")
                # 将字符串转换为浮点数
                float_value = float(percentage_string_without_percent)
                return float_value
            except Exception as e:
                log("字符串不能转换为浮点数")
                return None


        def 预计几率计算(预期, 抽奖次数, 中奖几率, 几率, 几率1, 几率2, 几率值, 几率1值, 几率2值):
            # 每次中奖后获得的期望值
            预期 = float(预期)
            几率 = 移除(几率)
            几率1 = 移除(几率1)
            几率2 = 移除(几率2)
            中奖几率 = 移除(中奖几率)

            几率值 = float(几率值)
            几率1值 = float(几率1值)
            几率2值 = float(几率2值)

            E = 几率值 * (几率 / 100) + 几率1值 * (几率1 / 100) + 几率2值 * (几率2 / 100)

            N = float(抽奖次数) * float(中奖几率 / 100)

            E_total = int(N) * int(E)

            # 标准差
            std_dev = math.sqrt(N)
            std_dev = std_dev * E

            if std_dev == 0:
                std_dev = 1

            # 计算标准分数Z
            Z = (预期 - E_total) / std_dev

            # 使用标准正态分布的累计分布函数计算概率
            probability = 1 - cumulative_distribution_function(Z)
            probability = float(probability)
            probability = "{:.2%}".format(probability)

            return probability

    if "抽奖":
        def 去宝箱界面():
            退出()
            # 签到()
            if True:
                if 加入战斗():
                    if not tu("宝箱入口", 0, 1, 1, 62, 269, 240, 419, 0, 0.7, 1):
                        click(155, 327)
                        time.sleep(0.5)

                if tu("2", 1, 1, 1, 24, 0, 145, 134):
                    click(260, 388)
                    time.sleep(0.5)
                else:
                    if 加入战斗():
                        if not tu("宝箱入口", 0, 1, 1, 62, 269, 240, 419, 0, 0.7, 1):
                            click(155, 327)
                            time.sleep(0.5)

                    if tu("2", 1, 1, 1, 24, 0, 145, 134):
                        click(260, 388)


        def 完成():
            # FindColors.find(
            #     "623,365,#97711B|616,362,#CCA654|608,336,#B07509|655,197,#E0E0E0|510,188,#4D88A4|735,192,#4D88A4",
            #     rect=[359, 133, 936, 596], diff=0.90) or FindColors.find(
            #     "653,346,#D54936|713,215,#4D88A4|524,204,#4D88A4|614,346,#2E3336|659,325,#FDE5DF|660,307,#E1E3E8",
            #     rect=[359, 133, 936, 596], diff=0.98) or tu("3", 1, 1, 1, 465, 234, 813, 490, 1,
            #                                                 0.8) or FindColors.find(
            #     "615,379,#4C4435|642,332,#E6E7E9|623,328,#DDE1E4|741,178,#4D88A4|528,193,#4D88A4|623,328,#DDE1E4",
            #     rect=[395, 139, 831, 548]) or FindColors.find(
            #     "613,349,#C3CDD6|676,199,#4D88A4|682,208,#4D88A4|670,385,#848484|635,363,#606368",
            #     rect=[420, 139, 915, 498], diff=0.90) or tu("银币", 1, 1, 1, 465, 234, 813, 490, 1,
            #                                                 0.8) or tu("票", 1, 1, 1, 455, 170, 837, 480, 0,
            #                                                            0.8) or FindColors.find(
            #     "543,199,#4D88A4|627,383,#7A634B|654,379,#7D644C|706,185,#4D88A4|757,203,#4D88A4",
            #     rect=[347, 123, 926, 574], diff=0.90) or FindImages.find_all_template([R.img("海战修理包.png"), ],
            #                                                                           rect=[450, 229, 807, 442],
            #                                                                           confidence=0.80, rgb=True)
            if Selector().type("WebView").find():
                Selector().text("Close").click().find()
                return False

            else:
                log("成功退出广告")
                Selector().text("Close").click().find()
                闪退()
                return True


        # 初始化事件
        def 跳():
            global 跳过成功
            if 跳过成功 == 0 and 广告结束 == 1:
                Selector().text("Close").click().find()
                Selector().text("关闭").click().find()


        def 跳6():
            if 跳过成功 == 0 and 广告结束 == 1:
                if Selector().text("已获得奖励").find() and 跳过成功 != 1:
                    click(1229, 44)


        def 跳1():
            global 跳过成功
            if 跳过成功 == 0 and 广告结束 == 1:
                if tu("跳过广告", 0, 1, 1, 2, 19, 104, 116, 0, 0.7, 1):
                    跳过成功 = 1


        def 跳2():
            global 跳过成功
            if 跳过成功 == 0 and 广告结束 == 1:
                if tu("跳过广告1", 0, 1, 1, 2, 19, 104, 116, 0, 0.7, 1):
                    跳过成功 = 1


        def 跳3():
            global 跳过成功

            if 跳过成功 == 0 and 广告结束 == 1:
                if tu("跳过广告", 0, 1, 1, 1076, 5, 1280, 138, 0, 0.7, 1):
                    跳过成功 = 1


        def 跳4():
            global 跳过成功
            if 跳过成功 == 0 and 广告结束 == 1:
                if tu("跳过广告1", 0, 1, 1, 1076, 5, 1280, 138, 0, 0.7, 1):
                    跳过成功 = 1


        def 跳5():
            global 跳过成功
            if 跳过成功 == 0 and 广告结束 == 1:
                if tu("跳过广告", 0, 1, 1, 1146, 2, 1280, 85, 0, 0.7, 1):
                    跳过成功 = 1


        event = threading.Event()


        def check_and_skip_ad():
            global 跳过成功, 广告结束
            event = threading.Event()
            跳过成功 = 0
            广告结束 = 1
            while Selector().type("WebView").find() and 广告结束 == 1:
                if 完成():
                    event.set()
                    break

                Selector().text("Close").click().find()
                Selector().text("关闭").click().find()
                Selector().text("").click().find()
                跳广告1 = [
                    threading.Thread(target=跳),
                    threading.Thread(target=跳1),
                    threading.Thread(target=跳2),
                    threading.Thread(target=跳3),
                    threading.Thread(target=跳4),
                    threading.Thread(target=跳5),
                    threading.Thread(target=跳6),
                ]
                if not 完成():
                    for thread28 in 跳广告1:
                        thread28.start()
                else:
                    event.set()
                    break

                # 等待所有线程完成
                for thread28 in 跳广告1:
                    thread28.join()
                    thread28.join()
                    thread28.join()


        def 关闭():
            while not stop_event.is_set() and Selector().path("/FrameLayout/VideoView").find():
                Selector().text("Close").click().find()
                Selector().text("关闭").click().find()
                Selector().text("").click().find()
                Selector().text("Skip").click().find()


        广告结束了 = 0


        def 收获():
            global 无法识别, 广告结束了, 广告结束
            while not stop_event.is_set():
                广告结束了 = 0
                广告结束 = 1
                if not Selector().path("/FrameLayout/VideoView").find():
                    广告结束了 = 1
                    Selector().text("Close").click().find()
                    time.sleep(2)
                    click(546, 581)
                    time.sleep(0.3)
                    click(546, 581)
                    Selector().text("Close").click().find()
                    time.sleep(5)
                    if Selector().text("Close").click().find():
                        time.sleep(1)
                        click(730, 419)
                        time.sleep(0.3)
                        click(730, 419)
                        Selector().text("Close").click().find()
                        time.sleep(4)
                    if not stop_event.is_set():
                        cuowuciold = cuowuci
                        threads = [
                            threading.Thread(target=process_gold),
                            threading.Thread(target=process_fire_extinguisher),
                            threading.Thread(target=process_smoke),
                            threading.Thread(target=process_silver_coin),
                            threading.Thread(target=process_ticket),
                            threading.Thread(target=process_repair_kit),
                            threading.Thread(target=process_unknown_item)
                        ]

                        for thread in threads:
                            thread.start()
                        # 等待所有线程完成
                        for thread in threads:
                            thread.join()
                            thread.join()
                            thread.join()

                        bbbb = cuowuci - cuowuciold
                        if bbbb == 7:
                            无法识别 += 1
                        广告结束 = 1
                        return


    def 广告及收益(x=1):
        global 广告结束, 广告结束了, jinbi, miaohuo, yinbi, xiuli, piao, yanwu, qita, chi, liangci, qitacu, cuowuci, jinbi5, jinbi7, jinbi15, piao10, piao100, piao20, yingbi1000, yingbi1500, yingbi3000, thread
        global jinbici, miaohuoci, yinbici, xiulici, piaoci, yanwuci, qitaci, jinbiold, piaoold, yinbiold, 无法识别
        广告结束了 = 0
        广告结束 = 1
        log("等待跳过广告")
        time.sleep(2)
        if FindImages.find_all_template([R.img("纯黑.png"), ], confidence=0.95):
            click(546, 142)
            time.sleep(0.3)
            Selector().text("Privacy").click().find()
            time.sleep(0.5)
            Selector().text("Close").click().find()
            Selector().text("关闭").click().find()
            Selector().text("").click().find()
            if not Selector().text("").click().find() or not Selector().text("关闭").click().find():
                click(321, 79)
                Selector().text("Close").click().find()
                Selector().text("关闭").click().find()
                Selector().text("").click().find()
        # Selector().text("Privacy").click().find()
        # time.sleep(1.5)
        # if not Selector().text("").click().find() or not Selector().text("关闭").click().find():
        #     click(321, 79)
        time.sleep(7)
        # if FindImages.find_all_template([R.img("纯黑.png"), ], confidence=0.95):
        #     click(546, 142)
        #     time.sleep(0.3)
        #     Selector().text("Privacy").click().find()
        #     time.sleep(1.5)
        #     Selector().text("Close").click().find()
        #     Selector().text("关闭").click().find()
        #     Selector().text("").click().find()
        #     if not Selector().text("").click().find() or not Selector().text("关闭").click().find():
        #         click(321, 79)
        #         Selector().text("Close").click().find()
        #         Selector().text("关闭").click().find()
        #         Selector().text("").click().find()
        a = 0
        vv = 0
        b = 0
        # 创建并启动线程
        thread44 = threading.Thread(target=check_and_skip_ad)
        thread44.start()
        # 分析收获 = threading.Thread(target=收获)
        # 分析收获.start()
        关闭广告 = threading.Thread(target=关闭)
        关闭广告.start()
        while a <= 50:
            if a > 30 and FindImages.find_all_template([R.img("纯黑.png"), ], confidence=0.95):
                Selector().text("Privacy").click().find()
            Selector().text("Close").click().find()
            Selector().text("关闭").click().find()
            Selector().text("").click().find()

            if 闪退() or 重启过 == 1:
                return
            a += 1

            if 完成():
                break


            else:
                if Selector(1).text("Skip").click().find():
                    pass
                else:
                    Selector(1).maxTextLength(-1).depth(8).childCount(1).clickable(True).find()
                    time.sleep(0.5)
                    Selector(1).text("Close").click().find()

                    if Selector(1).text("Close").click().find():
                        time.sleep(1)
                    else:
                        Selector().text("Close").click().find()
                        Selector().text("关闭").click().find()
                        Selector().text("").click().find()
                        if 完成():
                            break
                        if 广告结束了 == 0 and tu("XX", 0, 1, 1, 1159, 5, 1277, 93):
                            click(1229, 44)
                            time.sleep(1)
                        else:
                            if 完成():
                                break
                            Selector(1).maxTextLength(-1).depth(8).childCount(1).clickable(True).find()
                            time.sleep(0.5)
                            if Selector(1).text("Close").click().find():
                                click(1229, 44)
                    Selector().text("Skip").click().find()

                time.sleep(1)
            if 广告结束了 == 0:
                click(1229, 44)
            if 完成():
                break
            else:
                if 广告结束了 == 0 and tu("XX", 0, 1, 1, 1159, 5, 1277, 93):
                    click(1229, 44)
                    time.sleep(1)
            if 完成():
                break
            else:

                if 广告结束了 == 0 and tu("XX", 0, 1, 1, 1159, 5, 1277, 93, 1):
                    click(1229, 44)
                    time.sleep(2)
                    if 完成():
                        break
        time.sleep(2)
        log("跳过广告成功")
        thread44.join()
        Selector().text("Close").click().find()

        广告结束 = 0
        # 分析收获.join()
        if x == 1:
            log("开始抽奖")
            Selector().text("Close").click().find()
            time.sleep(2)
            click(546, 581)
            time.sleep(0.3)
            click(546, 581)
            time.sleep(2)
            if Selector().text("Close").click().find():
                time.sleep(1)
                click(730, 419)
                time.sleep(0.3)
                click(730, 419)
                Selector().text("Close").click().find()
                time.sleep(4)
            if not stop_event.is_set():
                cuowuciold = cuowuci
                threads = [
                    threading.Thread(target=process_gold),
                    threading.Thread(target=process_fire_extinguisher),
                    threading.Thread(target=process_smoke),
                    threading.Thread(target=process_silver_coin),
                    threading.Thread(target=process_ticket),
                    threading.Thread(target=process_repair_kit),
                    threading.Thread(target=process_unknown_item)
                ]

                for thread in threads:
                    thread.start()
                # 等待所有线程完成
                for thread in threads:
                    thread.join()
                    thread.join()
                    thread.join()

                bbbb = cuowuci - cuowuciold
                if bbbb == 7:
                    无法识别 += 1
            time.sleep(1)
            click(560, 581)
        elif x==2:
            log("领取金币")
            jinbi+=10
            chi += 1

        else:
            chi += 1
            无法识别 += 1


    kanchi = 0
    def 抽奖(x=0):
        global jinbi, miaohuo, yinbi, xiuli, piao, yanwu, liangci, 重启过, wwwwc, 网络问题, 无法识别,单次游戏局数
        bb = 1
        log("判断是否可以看广告")

        bb == 1
        ssguang = 0
        kanchi = 0
        wwwwc = 0
        网络问题局部 = 0
        重启过 = 0
        切换加速 = 0

        while bb == 1:

            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
            time.sleep(2)
            过 = 1
            if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.80):
                click(560, 581)

            if not tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7) and not zi("RE", 0, 672,582,983,695, 1):
                if kanchi == 1:

                    while wwwwc <= 8:
                        if stop_event.is_set():
                            return
                        if 闪退() or 重启过 == 1:
                            return
                        if tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7):
                            过 = 0
                            wwwwc += 30
                        else:
                            time.sleep(1)

                            wwwwc += 1
            if 过 != 0:
                if Ocr.mlkitocr_v2(rect=[701, 610, 945, 683], pattern='进行游戏') or Ocr.mlkitocr_v2(rect =[672,582,983,695],pattern = 'RE'):
                    if not tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7):
                        log("不可以，进行一局游戏")
                        return

                else:
                    if tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7) or zi("RE", 0, 672,582,983,695, 1):
                        过 = 0
                    else:
                        time.sleep(1.5)
                        if tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7) or zi("RE", 0, 672,582,983,695, 1):
                            过 = 0
                        else:
                            退出()
                            if 去宝箱界面():
                                log("重新进入宝箱界面")
                                continue
                            else:
                                闪退()
                                continue

            if 过 == 0:
                if tu("观看", 0, 1, 1, 658, 574, 969, 701, 0, 0.7) or zi("RE", 0, 672,582,983,695, 1):
                    log("可以观看")
                    if Ocr.mlkitocr_v2(rect=[273, 153, 1010, 575], pattern='tomorrow'):
                        time.sleep(1)
                        click(687, 479)
                        单次游戏局数 = 20
                        return
                    time.sleep(2)
                    tt = 1
                    while tt == 1:
                        if not tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7) and not Ocr.mlkitocr_v2(
                                rect=[701, 610, 945, 683], pattern='进行游戏') and not tu("2", 1, 1, 1, 24, 0, 145,
                                                                                          134, 0) and not zi("观看",
                                                                                                             1, 686,
                                                                                                             582,
                                                                                                             966,
                                                                                                             709,
                                                                                                             1) and not zi("RE", 0, 672,582,983,695, 1):
                            去宝箱界面()
                        if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                            click(640, 524)
                        time.sleep(3)
                        if stop_event.is_set():
                            return
                        if 闪退() or 重启过 == 1:
                            return
                        if Selector().type("WebView").find():
                            break
                        if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                            time.sleep(5)
                            网络问题局部 += 1
                            zi("取消", 0, 499, 343, 791, 491, 1)
                            tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                            if Selector().type("WebView").find():
                                break
                        else:
                            if zi("取消", 0, 499, 343, 791, 491, 1):
                                网络问题局部 += 1
                            if Selector().type("WebView").find():
                                break

                            if tu("观看", 0, 1, 1, 658, 574, 969, 701, 0, 0.7) or zi("RE", 0, 672,582,983,695, 1):
                                zi("观看", 1, 686, 582, 966, 709, 1)
                                zi("RE", 0, 672,582,983,695, 1)
                        if Ocr.mlkitocr_v2(rect=[273, 153, 1010, 575], pattern='tomorrow'):
                            time.sleep(1)
                            click(687, 479)
                            单次游戏局数 = 20

                            return
                        if Selector().type("WebView").find():
                            break

                        if 服务器():
                            网络问题局部 += 1
                        if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                            网络问题局部 += 1
                        if tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7):
                            tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                            time.sleep(2)
                            if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                                网络问题局部 += 1
                        if 网络问题局部 >= 3:
                            切换加速 += 1
                            网络问题局部 = 0
                            if 切换加速 == 13:
                                切换加速=0
                                重启()
                                去宝箱界面()
                                切换加速器()
                                continue
                            切换加速器()

                            time.sleep(3)
                            continue

                        if Selector().type("WebView").find():
                            break
                        if Ocr.mlkitocr_v2(rect=[701, 610, 945, 683], pattern='进行游戏'):
                            return
                    log("未出现问题")
                else:
                    if zi("观看", 1, 686, 582, 966, 709, 1) or zi("RE", 0, 672,582,983,695, 1):
                        log("可以观看")
                        time.sleep(2)
                        tt = 1
                        while tt == 1:
                            if not tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7) and not Ocr.mlkitocr_v2(
                                    rect=[701, 610, 945, 683], pattern='进行游戏') and not tu("2", 1, 1, 1, 24, 0,
                                                                                              145,
                                                                                              134, 0) and not zi(
                                "观看", 1, 686, 582, 966, 709, 1) and not zi("RE", 0, 672,582,983,695, 1):
                                去宝箱界面()
                            if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                                click(640, 524)
                            time.sleep(3)
                            if stop_event.is_set():
                                return
                            if 闪退() or 重启过 == 1:
                                return
                            if Selector().type("WebView").find():
                                break
                            if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                                time.sleep(5)
                                网络问题局部 += 1
                                if Selector().type("WebView").find():
                                    break
                            else:
                                if Selector().type("WebView").find():
                                    break


                                if tu("观看", 0, 1, 1, 658, 574, 969, 701, 0, 0.7) or zi("RE", 0, 672,582,983,695, 1):
                                    zi("观看", 1, 686, 582, 966, 709, 1)
                            if Ocr.mlkitocr_v2(rect=[273, 153, 1010, 575], pattern='tomorrow'):
                                time.sleep(1)
                                click(687, 479)
                                单次游戏局数 = 20
                                return
                            if Selector().type("WebView").find():
                                break
                            if tu("观看", 1, 1, 1, 658, 574, 969, 701, 0, 0.7) and zi("RE", 1, 672,582,983,695, 1):
                                tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                                time.sleep(2)
                                if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                                    网络问题 += 1
                                    网络问题局部 += 1
                            if 服务器():
                                网络问题局部 += 1
                            if 网络问题局部 >= 3:
                                切换加速 += 1
                                网络问题局部 = 0
                                if 切换加速 == 10:
                                    重启()
                                    去宝箱界面()
                                    切换加速器()
                                    continue
                                切换加速器()

                                time.sleep(3)
                                continue

                            if Selector().type("WebView").find():
                                break
                            if Ocr.mlkitocr_v2(rect=[701, 610, 945, 683], pattern='进行游戏'):
                                return
                        log("未出现问题")

            # if not tu("电池", 1, 1, 1, 1184, 8, 1216, 27, 0) and not Ocr.mlkitocr_v2(rect=[1095, 626, 1203, 674],
            #                                                                          pattern='.*10.*'):
            if Selector().type("WebView").find():
                广告及收益()
                网络问题局部 = 0
                kanchi += 1


    if "意外修正":
        取消成功 = 0

        goumaizhong=1
        def 点击取消():
            global 取消成功, 游戏结束, 下载中,goumaizhong
            下载中 = 0
            zi("退出", 0, 480, 427, 805, 563, 1)
            if zi('获得', 0, 940, 583, 1237, 717, 1):
                time.sleep(5)
            if zi('购买', 0, 329,300,1227,697, 1):
                goumaizhong=0
                time.sleep(5)
                zi('购买', 0, 724, 433, 991, 555, 1)
                time.sleep(3)
                zi('取消', 0, 308, 453, 580, 547, 1)
                time.sleep(3)
                退出()
                time.sleep(5)
                if zi("稍后", 0, 623, 453, 1268, 717, 1):
                    time.sleep(5)
                    goumaizhong = 1
                    退出()
                goumaizhong = 1
            zi("稍后", 0, 377, 594, 1251, 701, 1)
            下载中 = 0
            if zi("下载", 0, 505, 296, 1073, 673, 1):
                下载中 = 1
                time.sleep(100)
                下载中 = 0

            if zi("返回", 0, 14, 513, 1265, 714, 1):
                游戏结束 = 1
            if zi("返回基地", 0, 19, 561, 348, 711, 1) or zi("返回港口", 0, 19, 561, 348, 711, 1):
                游戏结束 = 1
            if 正在匹配游戏 == 0 and Ocr.mlkitocr_v2(rect=[311, 144, 1061, 564], pattern='连接丟失'):
                click(645, 496)

            if not Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651], pattern='更新'):
                取消成功 = 1
                zi("取消", 0, 322, 439, 563, 549, 1)


        def 退出():
            wqww = threading.Thread(target=点击取消)
            # 启动线程
            wqww.start()
            签到()
            if  goumaizhong==0:
                time.sleep(20)
            if 取消成功 == 1 or tu("2", 1, 1, 1, 24, 0, 145, 134, 0, 0.8, 1) or tu("2", 1, 1, 1, 24, 0, 145, 134, 1,
                                                                                   0.8, 1):
                if tu("福利", 0, 1, 1, 52, 52, 656, 431, 1, 0.8, 1):
                    time.sleep(15)
                    if zi("继续", 0, 526, 453, 798, 609, 1):
                        pass
                if 下载中 == 0 and tu("2", 0, 1, 1, 24, 0, 145, 134, 0) or tu("2", 0, 1, 1, 24, 0, 145, 134, 1):
                    adadad = 1
                    while adadad == 1 and not stop_event.is_set():

                        if 下载中 == 1:
                            time.sleep(5)
                            continue
                        崩溃进程()
                        if tu("2", 0, 1, 1, 24, 0, 145, 134, 0) or tu("2", 0, 1, 1, 24, 0, 145, 134, 1):

                            time.sleep(0.5)
                        else:
                            adadad += 2
                            签到()
                        if 加入战斗():
                            pass
                        else:
                            zi("取消", 0, 322, 439, 563, 549, 1)
                            if zi("稍后", 1, 623, 453, 1268, 717, 1):
                                time.sleep(4)
                                click(815, 649)
                                time.sleep(3)
                                退出()
                                time.sleep(3)


        def 闪退():
            global 重启过
            if not Selector().packageName("com.gaijingames.wtm").find() and not Selector().type("WebView").find():
                if stop_event.is_set():
                    return
                time.sleep(5)
                启动()
                重启过 = 1

                return True
            return False


        def download_chunk(url, headers, start, end, filename):
            headers['Range'] = f'bytes={start}-{end}'
            response = requests.get(url, headers=headers)
            with open(filename, 'rb+') as f:
                f.seek(start)
                f.write(response.content)
                downloaded_bytes = end - start + 1
                progress_mb = round(downloaded_bytes / 1024 / 1024, 2)
                log(f"线程 {threading.current_thread().name} 已下载 {progress_mb} MB")
                return downloaded_bytes


        def download_apk(url, local_filename):
            headers = {}
            response = requests.head(url, headers=headers)
            file_size = int(response.headers['Content-Length'])

            chunk_size = 1024 * 1024  # 1 MB
            num_threads = 32

            chunk_sizes = [chunk_size] * num_threads
            for i in range(file_size % num_threads):
                chunk_sizes[i] += file_size // num_threads

            threads = []
            with open(local_filename, 'wb') as f:
                for i in range(num_threads):
                    start = i * chunk_size
                    end = start + chunk_sizes[i] - 1
                    t = Thread(target=download_chunk, args=(url, headers, start, end, f.name))
                    threads.append(t)
                    t.start()

                start_time = datetime.now()
                while threads:
                    alive_threads = [t for t in threads if t.is_alive()]
                    if alive_threads:
                        for t in alive_threads:
                            progress = t.join(timeout=5)
                            if progress is not None:
                                progress_mb = round(progress / 1024 / 1024, 2)
                                log(f"线程 {t.name} 已下载 {progress_mb} MB")
                    else:
                        threads.clear()

            end_time = datetime.now()
            download_duration = (end_time - start_time).total_seconds()
            log(f'Download complete: {local_filename}，下载时长：{download_duration}秒')


        def 更新1():
            global 更新shu
            log("开始更新游戏")
            加时间(5)
            更新shu+=1
            if 是否接受bug信息控制字 == 0:
                email_song(f'{用户邮箱},{设备号}开始更新游戏',
                       f'"开始更新游戏",初始时间加5分钟即将重启软件,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                       f'{报告邮箱}', 4)
            if 是否接受bug信息用户 == 0:
                email_song('开始更新游戏',
                       f'"开始更新游戏",初始时间加5分钟即将重启软件,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                       f'{用户邮箱}', 4)

            url = "https://wtmobile.com/apk"
            save_path = "/storage/emulated/0/Download/wtmobile.apk"
            max_retries = 5  # 最大重试次数
            retry_delay = 5  # 重试间隔时间（秒）
            chunk_size = 1024  # 每次读取的字节数
            progress_interval = 5  # 进度反馈间隔（秒）

            retries = 0
            while retries < max_retries:
                response = None
                try:
                    response = requests.get(url, stream=True, timeout=60)  # 增加超时时间
                    if response.status_code == 200:
                        total_size = int(response.headers.get('content-length', 0))
                        downloaded_size = 0
                        last_progress_time = time.time()
                        with open(save_path, 'wb') as out_file:
                            for data in response.iter_content(chunk_size=chunk_size):
                                if data:
                                    out_file.write(data)
                                    downloaded_size += len(data)
                                    current_time = time.time()
                                    if current_time - last_progress_time >= progress_interval:
                                        log(f"下载进度: {downloaded_size / total_size * 100:.2f}%")
                                        last_progress_time = current_time
                        log(f"APK文件已成功下载并保存到: {save_path}")
                        break  # 下载成功，退出循环
                    else:
                        log(f"下载失败，HTTP状态码: {response.status_code}")
                        break  # 下载失败，退出循环
                except requests.exceptions.RequestException as e:
                    log(f"下载过程中发生错误: {e}")
                    retries += 1
                    if retries < max_retries:
                        log(f"重试下载，第 {retries} 次，等待 {retry_delay} 秒...")
                        time.sleep(retry_delay)
                    else:
                        log("已达到最大重试次数，下载失败。")
                finally:
                    if response is not None:
                        response.close()

            time.sleep(15)
            # 打开文件管理

            if 设备 == 1:
                Intent.run("com.android.filemanager")

                time.sleep(5)
                # 安装
                time.sleep(5)
                node = Selector().text("War Thunder Mobile").find()
                if node:
                    click(613, node.center_y)
                else:
                    res = Ocr.paddleocr_v2(rect=[117, 148, 187, 838], pattern='War')
                    if res:
                        # 循环打印识别到的每一个段落
                        for r in res:
                            log("文字:", r.text)
                            log("文字中心坐标:", r.center_x, r.center_y)
                            log("文字范围:", r.rect)
                            click(617, r.center_y)
                    else:
                        log("未找到匹配的文本")
                        click(628, 202)
                time.sleep(2.5)
                # 点击安装
                if Selector().text("安装").click().find():
                    click(582, 765)
                time.sleep(13)
                action.Key.back()
                time.sleep(0.5)

                action.Key.recents()
                time.sleep(4)
                click(630, 1114)
                time.sleep(0.5)
            else:
                Intent.run("com.coloros.filemanager")

                time.sleep(5)
                # 安装

                time.sleep(2)

                time.sleep(2)
                click(196, 388)
                time.sleep(2)
                Selector().text("重新安装").click().find()
                time.sleep(30)
                Selector().text("继续安装").click().find()
                time.sleep(25)
                action.Key.back()
                time.sleep(1)
                action.Key.back()
                time.sleep(1)
                Selector().text("Download").click().find()


        # 案例:打开AirSctipt 官网
        # 导包
        from ascript.android import system
        # 模拟在 控件检查器查到的 文本框中输入‘你好 aslib!’
        from ascript.android import action
        from ascript.android.node import Selector


        def 更新():
            global 更新shu
            log("开始更新游戏")
            加时间(5)
            更新shu+=1
            time.sleep(2)
            Intent.run("com.android.settings")
            time.sleep(5)
            Selector().id("com.android.settings:id/search_action_bar").click().find()

            time.sleep(2)

            action.input("QQ")
            time.sleep(2)
            Selector().packageName("com.android.settings.intelligence").type("LinearLayout").click().find()
            time.sleep(2)
            Selector().text("启用").click().find()
            time.sleep(3)
            try:
                system.browser("https://wtmobile.com/apk")
            except Exception as e:
                log(e)
            time.sleep(10)
            time.sleep(1)
            Selector().text("进入").click().find()
            time.sleep(2)
            fffs = 1
            while fffs == 1:
                if Selector().type("LinearLayout").packageName("com.tencent.mtt").childCount(1).drawingOrder(
                        3).click().find():
                    fffs += 1
                if Selector().text("安装").click().find():
                    fffs += 1
                time.sleep(8)
                Selector().desc("刷新").click().find()
            time.sleep(3)
            Selector().id("com.tencent.mtt:id/mainButtonCardView").click().find()
            Selector().packageName("com.tencent.mtt").type("LinearLayout").inputType(0).childCount(1).drawingOrder(
                2).click().find()
            time.sleep(1)
            Selector().id("com.tencent.mtt:id/mainButtonCardView").click().find()
            fffs = 1
            while fffs == 1:
                if Selector().text("安装").click().find():
                    fffs += 1
                time.sleep(3)
                if Selector().text("安装").click().find():
                    fffs += 1

            time.sleep(10)
            action.Key.recents()
            time.sleep(0.1)
            action.Key.recents()
            time.sleep(1)
            if not Selector().text("停用").click().find():
                action.Key.recents()
                time.sleep(0.1)
                action.Key.recents()
                time.sleep(1)
                if not Selector().text("停用").click().find():
                    action.Key.recents()
                    time.sleep(0.1)
                    action.Key.recents()
                    time.sleep(1)
            time.sleep(1)
            if not Selector().text("停用应用").click().find():
                time.sleep(2)
                Intent.run("com.android.settings")
                time.sleep(5)
                Selector().id("com.android.settings:id/search_action_bar").click().find()

                time.sleep(2)

                action.input("QQ")
                time.sleep(2)
                Selector().packageName("com.android.settings.intelligence").type("LinearLayout").click().find()
                time.sleep(2)
                Selector().text("停用").click().find()
                time.sleep(1)
                Selector().text("停用应用").click().find()
                time.sleep(1)
            time.sleep(1)

        def 切换模式(海1陆2空3=1):
            if 加入战斗():
                if zi("切换军种", 0, 84, 115, 249, 195, 1):
                    time.sleep(1)
                    if Ocr.mlkitocr_v2(rect=[21, 129, 725, 283], pattern='载具') or Ocr.mlkitocr_v2(rect =[82,395,450,522],pattern = '海战') or Ocr.mlkitocr_v2(rect =[455,403,818,535],pattern = '陆战') or Ocr.mlkitocr_v2(rect =[846,379,1225,577],pattern = '空战'):
                        if 海1陆2空3 == 1:
                            if not zi("海", 0, 38, 407, 1239, 580):
                                click(249, 424)
                        elif 海1陆2空3 == 2:
                            if not zi("陆", 0, 38, 407, 1239, 580):
                                click(680, 377)
                        elif 海1陆2空3 == 3:
                            if not zi("空", 0, 38, 407, 1239, 580):
                                click(1051, 424)

                else:
                    退出()
                    if zi("切换军种", 0, 84, 115, 249, 195, 1):
                        time.sleep(1)
                        if Ocr.mlkitocr_v2(rect=[21, 129, 725, 283], pattern='载具') or Ocr.mlkitocr_v2(rect =[82,395,450,522],pattern = '海战') or Ocr.mlkitocr_v2(rect =[455,403,818,535],pattern = '陆战') or Ocr.mlkitocr_v2(rect =[846,379,1225,577],pattern = '空战'):
                            if 海1陆2空3 == 1:
                                if not zi("海", 0, 38, 407, 1239, 580):
                                    click(249, 424)
                            elif 海1陆2空3 == 2:
                                if not zi("陆", 0, 38, 407, 1239, 580):
                                    click(680, 377)
                            elif 海1陆2空3 == 3:
                                if not zi("空", 0, 38, 407, 1239, 580):
                                    click(1051, 424)
                    else:
                        click(159, 167)
                        time.sleep(1)
                        time.sleep(1)
                        if Ocr.mlkitocr_v2(rect=[21, 129, 725, 283], pattern='载具') or Ocr.mlkitocr_v2(rect =[82,395,450,522],pattern = '海战') or Ocr.mlkitocr_v2(rect =[455,403,818,535],pattern = '陆战') or Ocr.mlkitocr_v2(rect =[846,379,1225,577],pattern = '空战'):
                            if 海1陆2空3 == 1:
                                if not zi("海", 0, 38, 407, 1239, 580):
                                    click(249, 424)
                            elif 海1陆2空3 == 2:
                                if not zi("陆", 0, 38, 407, 1239, 580):
                                    click(680, 377)
                            elif 海1陆2空3 == 3:
                                if not zi("空", 0, 38, 407, 1239, 580):
                                    click(1051, 424)

                退出()
            else:
                退出()
                if 加入战斗():
                    if zi("切换军种", 0, 84, 115, 249, 195, 1):
                        time.sleep(1)
                        if Ocr.mlkitocr_v2(rect=[21, 129, 725, 283], pattern='载具') or Ocr.mlkitocr_v2(rect =[82,395,450,522],pattern = '海战') or Ocr.mlkitocr_v2(rect =[455,403,818,535],pattern = '陆战') or Ocr.mlkitocr_v2(rect =[846,379,1225,577],pattern = '空战'):
                            if 海1陆2空3 == 1:
                                if not zi("海", 0, 38, 407, 1239, 580):
                                    click(249, 424)
                            elif 海1陆2空3 == 2:
                                if not zi("陆", 0, 38, 407, 1239, 580):
                                    click(680, 377)
                            elif 海1陆2空3 == 3:
                                if not zi("空", 0, 38, 407, 1239, 580):
                                    click(1051, 424)
                        退出()
                        if not  zi("切换军种", 0, 84, 115, 249, 195, 1):
                            time.sleep(1)
                            if 海1陆2空3 == 1:
                                if not zi("海", 0, 38, 407, 1239, 580):
                                    click(249, 424)
                            elif 海1陆2空3 == 2:
                                if not zi("陆", 0, 38, 407, 1239, 580):
                                    click(680, 377)
                            elif 海1陆2空3 == 3:
                                if not zi("空", 0, 38, 407, 1239, 580):
                                    click(1051, 424)
                        click(159, 167)
                        if Ocr.mlkitocr_v2(rect=[21, 129, 725, 283], pattern='载具') or Ocr.mlkitocr_v2(rect =[82,395,450,522],pattern = '海战') or Ocr.mlkitocr_v2(rect =[455,403,818,535],pattern = '陆战') or Ocr.mlkitocr_v2(rect =[846,379,1225,577],pattern = '空战'):
                            if 海1陆2空3 == 1:
                                if not zi("海", 0, 38, 407, 1239, 580):
                                    click(249, 424)
                            elif 海1陆2空3 == 2:
                                if not zi("陆", 0, 38, 407, 1239, 580):
                                    click(680, 377)
                            elif 海1陆2空3 == 3:
                                if not zi("空", 0, 38, 407, 1239, 580):
                                    click(1051, 424)
                    退出()


        def 反抢登():
            global 邮箱控制, 强行登录

            if 邮箱控制 == 1 or 强行登录 == 1:
                time.sleep(5)
                log("收到继续邮件，执行计算并更新时间() 和重启()")
                计算并更新时间()

                邮箱控制 = 0
                强行登录 = 0
                click(628, 501)
                time.sleep(3)
                click(682, 513)
                time.sleep(1)
                click(682, 513)

                asdd = 1
                asddddsa = 0
                while asdd == 1:
                    if 加入战斗():
                        if zi("取消", 0, 322, 439, 563, 549):
                            pass
                        asdd += 0.5
                    if zi("取消", 0, 322, 439, 563, 549):
                        pass
                    if zi("取消", 1, 311, 442, 572, 549) and Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651],
                                                                             pattern='更新'):
                        更新()
                        time.sleep(5)
                        Intent.run("com.gaijingames.wtm")
                        time.sleep(20)
                    if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern=' 稍后'):
                        time.sleep(4)
                        click(815, 649)
                        time.sleep(3)
                        退出()
                        time.sleep(3)
                        退出()
                    Selector().text("YES").click().find()
                    if tu("2", 0, 1, 1, 24, 0, 145, 134):
                        time.sleep(2)
                    if 签到():
                        time.sleep(2)
                    if tu("取消灰", 0, 1, 1, 280, 430, 583, 573):
                        tu("2", 0, 1, 1, 24, 0, 145, 134)
                        time.sleep(2)
                        签到()
                    if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                        tu("2", 0, 1, 1, 24, 0, 145, 134)
                        time.sleep(2)
                        签到()

                    time.sleep(2)
                    if 加入战斗():
                        if zi("取消", 0, 322, 439, 563, 549):
                            pass
                        asdd += 0.5
                    if asddddsa >= 50:
                        asdd += 1
                    else:
                        asddddsa += 1

                退出()
                time.sleep(4)
                # 切换载具
                click(127, 153)
                time.sleep(4)
                # 点击海战
                click(322, 462)
                time.sleep(4)
                退出()

                stop_event.clear()  # 清除停止事件状态
                continue_event.set()  # 设置继续事件，重新启动任务


            else:
                email_song(f'{用户邮箱},{设备号}错误操作', '未暂停便继续', f'{报告邮箱}', 4)
                email_song('错误操作', '错误操作\n请先暂停再继续.', f'{用户邮箱}', 4)


        def 抢登():
            if Ocr.paddleocr_v2(rect=[537, 205, 746, 294], pattern='连接错误'):
                return True
            if FindImages.find_all_template([R.img("5.png"), ], rect=[455, 422, 841, 609], confidence=0.95):
                time.sleep(10)
                if FindImages.find_all_template([R.img("5.png"), ], rect=[455, 422, 841, 609], confidence=0.95):
                    return True
            return False


        def 服务器():
            global 网络问题
            if zi("无回应", 1, 370, 151, 980, 552, 1) or FindImages.find_template([R.img("服务器.png"), ],
                                                                                  rect=[403, 203, 878, 568],
                                                                                  confidence=0.95, rgb=True):
                click(628, 503)
                time.sleep(1.5)
                网络问题 += 1
                return True
            else:
                return False


        def 签到():
            if Ocr.mlkitocr_v2(rect =[78,14,380,125],pattern = '登录奖励'):
                if not 加入战斗():
                    if FindColors.find(
                            "287,321,#C91208|292,333,#B31208|299,339,#9C1107|384,339,#A81208|390,332,#B71208|412,321,#CD1208",
                            rect=[46, 308, 1197, 591]):
                        time.sleep(10)
                        try:
                            zi('获得', 0, 4, 129, 1251, 643)
                            time.sleep(10)

                            tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7)

                            tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)

                            tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0)
                            time.sleep(5)
                            if zi('观看广告', 0, 21,140,1247,645, 1):
                                log("等待跳过广告")
                                time.sleep(5)
                                if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                                    time.sleep(5)
                                tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)

                                tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0)
                                广告及收益(0)
                        except Exception as e:
                            email_song(f'签到{设备号}', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}')

                        time.sleep(6)
                        退出()
                        退出()
                        return False
                if Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651], pattern='更新') and not tu("2", 1, 1, 1, 24, 0, 145, 134,
                                                                                          0, 0.8, 1):
                    重启(1)
                    重启过 == 1
        def 错误():
            stop_event.set()  # 设置停止事件，通知主线程停止
            continue_event.clear()  # 清除继续事件
            time.sleep(15)
            action.Key.recents()
            time.sleep(2)
            Selector().desc("移除War Thunder Mobile。").click().find()
            time.sleep(1)
            system.reboot(5000)

        def 重启(x=0):
            try:
                if True:
                    time.sleep(5)
                    action.Key.recents()
                    time.sleep(4)
                    if 设备 == 1:

                        Selector().desc("移除War Thunder Mobile。").click().find()
                        # time.sleep(0.5)
                        #
                        # click(909, 632)
                    else:
                        action.slide(350, 573, 645, 612)
                        time.sleep(0.5)

                    # 更新()
                    time.sleep(5)

                    Intent.run("com.gaijingames.wtm")
                    time.sleep(20)
                    if x == 1:
                        更新()
                        time.sleep(5)
                        Intent.run("com.gaijingames.wtm")
                        time.sleep(20)
                    if zi("取消", 1, 311, 442, 572, 549) and Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651],
                                                                             pattern='更新'):
                        更新()
                        time.sleep(5)
                        Intent.run("com.gaijingames.wtm")
                        time.sleep(20)
                    else:
                        zi("取消", 0, 311, 442, 572, 549)
                    asdd = 1
                    asddddsa = 0
                    while asdd == 1:

                        if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90],
                                           pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                                rect=[1027, 0, 1124, 45], pattern='PL') or not Ocr.mlkitocr_v2(rect=[1027, 0, 1124, 45],
                                                                                               pattern='PL') and Ocr.mlkitocr_v2(
                            rect=[791, 35, 1181, 90], pattern='\\d+') and 加入战斗():
                            if zi("取消", 0, 322, 439, 563, 549) and not Ocr.mlkitocr_v2(rect=[690, 422, 1036, 572],
                                                                                         pattern='更新'):
                                pass
                            asdd += 0.5
                        if zi("取消", 0, 322, 439, 563, 549):
                            pass
                        if zi("取消", 1, 311, 442, 572, 549) and Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651],
                                                                                 pattern='更新') or Ocr.mlkitocr_v2(
                            rect=[690, 422, 1036, 572], pattern='更新') and not tu("2", 1, 1, 1, 24, 0, 145, 134, 0,
                                                                                   0.8, 1):
                            更新()
                            time.sleep(5)
                            Intent.run("com.gaijingames.wtm")
                            time.sleep(20)

                        if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern=' 稍后'):
                            time.sleep(4)
                            click(815, 649)
                            time.sleep(3)
                            退出()
                            time.sleep(3)
                            退出()
                        Selector().text("YES").click().find()
                        if tu("2", 0, 1, 1, 24, 0, 145, 134):
                            time.sleep(2)
                        if 签到():
                            time.sleep(2)
                        if tu("取消灰", 0, 1, 1, 280, 430, 583, 573):
                            tu("2", 0, 1, 1, 24, 0, 145, 134)
                            time.sleep(2)
                            签到()
                        if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                            tu("2", 0, 1, 1, 24, 0, 145, 134)
                            time.sleep(2)
                            签到()

                        time.sleep(2)
                        if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90],
                                           pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                                rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                                           pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                            rect=[1027, 0, 1124, 45], pattern='PL'):
                            if zi("取消", 0, 322, 439, 563, 549):
                                pass
                            asdd += 0.5
                        if zi('购买', 0, 940, 583, 1237, 717, 1):
                            time.sleep(5)
                            zi('购买', 0, 59, 345, 654, 717)
                            time.sleep(5)
                            zi('购买', 0, 724, 433, 991, 555)
                            time.sleep(3)
                            zi('取消', 0, 308, 453, 580, 547)
                            time.sleep(3)
                            退出()
                            time.sleep(5)
                            if zi("稍后", 0, 662, 592, 937, 708):
                                time.sleep(5)
                                退出()
                        zi("已获得", 0, 10, 173, 1267, 477)
                        闪退()
                        if asddddsa >= 100:
                            asdd += 1
                        else:
                            asddddsa += 1
                        退出()
                        签到()

                    退出()
                    if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                            rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                                       pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                        rect=[1027, 0, 1124, 45], pattern='PL'):
                        if zi("取消", 0, 322, 439, 563, 549):
                            pass
                        asdd += 0.5
                    zi("已获得", 0, 10, 173, 1267, 477, 1)
                    zi("取消", 0, 322, 439, 563, 549)
                    if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern=' 稍后'):
                        time.sleep(4)
                        click(815, 649)
                        time.sleep(3)
                        退出()
                        time.sleep(3)
                    退出()

                    # time.sleep(4)
                    # # 切换载具
                    # click(127, 153)
                    # time.sleep(4)
                    # # 点击海战
                    # click(322, 462)
                    # time.sleep(4)
                    # 退出()
            except Exception as e:
                    email_song(f'{设备号}重启错误{用户邮箱}', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}', 5)
                    错误()

        def 启动(x=0):
            if Selector().packageName("com.gaijingames.wtm").find():
                return
            else:
                Intent.run("com.gaijingames.wtm")
                time.sleep(5)
                if x == 1:
                    更新()
                    time.sleep(5)
                    Intent.run("com.gaijingames.wtm")
                    time.sleep(20)
                if zi("取消", 1, 311, 442, 572, 549) and Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651],
                                                                         pattern='更新'):
                    更新()
                    time.sleep(5)
                    Intent.run("com.gaijingames.wtm")
                    time.sleep(20)
                else:
                    zi("取消", 0, 311, 442, 572, 549)
                asdd = 1
                asddddsa = 0
                while asdd == 1:

                    if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                            rect=[1027, 0, 1124, 45], pattern='PL') or not Ocr.mlkitocr_v2(rect=[1027, 0, 1124, 45],
                                                                                           pattern='PL') and Ocr.mlkitocr_v2(
                        rect=[791, 35, 1181, 90], pattern='\\d+') and 加入战斗():
                        if zi("取消", 0, 322, 439, 563, 549) and not Ocr.mlkitocr_v2(rect=[690, 422, 1036, 572],
                                                                                     pattern='更新'):
                            pass
                        asdd += 0.5
                    if zi("取消", 0, 322, 439, 563, 549):
                        pass
                    if zi("取消", 1, 311, 442, 572, 549) and Ocr.mlkitocr_v2(rect=[152, 141, 1152, 651],
                                                                             pattern='更新') or Ocr.mlkitocr_v2(
                        rect=[690, 422, 1036, 572], pattern='更新') and not tu("2", 1, 1, 1, 24, 0, 145, 134, 0, 0.8,
                                                                               1):
                        更新()
                        time.sleep(5)
                        Intent.run("com.gaijingames.wtm")
                        time.sleep(20)

                    if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern=' 稍后'):
                        time.sleep(4)
                        click(815, 649)
                        time.sleep(3)
                        退出()
                        time.sleep(3)
                        退出()
                    Selector().text("YES").click().find()
                    if tu("2", 0, 1, 1, 24, 0, 145, 134):
                        time.sleep(2)
                    if 签到():
                        time.sleep(2)
                    if tu("取消灰", 0, 1, 1, 280, 430, 583, 573):
                        tu("2", 0, 1, 1, 24, 0, 145, 134)
                        time.sleep(2)
                        签到()
                    if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                        tu("2", 0, 1, 1, 24, 0, 145, 134)
                        time.sleep(2)
                        签到()

                    time.sleep(2)
                    if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                            rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                                       pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                        rect=[1027, 0, 1124, 45], pattern='PL'):
                        if zi("取消", 0, 322, 439, 563, 549):
                            pass
                        asdd += 0.5
                    if zi('购买', 0, 940, 583, 1237, 717, 1):
                        time.sleep(5)
                        zi('购买', 0, 59, 345, 654, 717)
                        time.sleep(5)
                        zi('购买', 0, 724, 433, 991, 555)
                        time.sleep(3)
                        zi('取消', 0, 308, 453, 580, 547)
                        time.sleep(3)
                        退出()
                        time.sleep(5)
                        if zi("稍后", 0, 662, 592, 937, 708):
                            time.sleep(5)
                            退出()
                    zi("已获得", 0, 10, 173, 1267, 477)
                    闪退()
                    if asddddsa >= 100:
                        asdd += 1
                    else:
                        asddddsa += 1
                    退出()
                    签到()

                退出()
                if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                        rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                                   pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL'):
                    if zi("取消", 0, 322, 439, 563, 549):
                        pass
                    asdd += 0.5
                zi("已获得", 0, 10, 173, 1267, 477, 1)
                zi("取消", 0, 322, 439, 563, 549)
                if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern=' 稍后'):
                    time.sleep(4)
                    click(815, 649)
                    time.sleep(3)
                    退出()
                    time.sleep(3)
                退出()


        def 任务():
            global 暂时不购买
            log("开始每日任务")
            if 加入战斗():
                time.sleep(2)
            else:
                zi("取消", 0, 322, 439, 563, 549)
                time.sleep(2)
                if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern='稍后'):
                    time.sleep(4)
                    click(815, 649)
                    time.sleep(3)
                    退出()
                    time.sleep(3)
                退出()
            退出()
            time.sleep(4)
            # 切换载具
            切换模式(1)
            退出()
            text = 0
            if 加入战斗():
                time.sleep(2)
            else:
                zi("取消", 0, 322, 439, 563, 549)
                time.sleep(2)
                if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern=' 稍后'):
                    time.sleep(4)
                    click(815, 649)
                    time.sleep(3)
                    退出()
                    time.sleep(3)
                    退出()
                退出()

            if True:
                x = 183
                aaddc = 1
                # 买东西加免费的东西
                if 加入战斗():
                    log("开始买东西")
                    click(1039, 73)
                    time.sleep(1.5)
                    购买 = 0
                    aadcc = 1
                    while aaddc <= 6:

                        aaddc += 1
                        time.sleep(2)
                        click(221, x)
                        if aadcc == 1:
                            time.sleep(2)
                        暂时不购买 = 1
                        if aadcc == 1 and 箱子 != 0 and Ocr.mlkitocr_v2(rect=[404, 592, 778, 700], pattern='31'):
                            有箱子 = 1
                            aadcc = 0
                            text=99999999
                            log("有箱子")

                            if 箱子 == 1:
                                if text > 350000:
                                    购买 = 1
                                else:
                                    暂时不购买 = 0
                                    购买 = 0
                            elif 箱子 == 2:
                                if text > 350000:
                                    购买 = 1
                                else:
                                    暂时不购买 = 0
                                    购买 = 0
                            elif 箱子 == 3:
                                if text > 700000:
                                    购买 = 2
                                else:
                                    暂时不购买 = 0
                                    购买 = 0
                            if 暂时不购买 == 1 and Ocr.mlkitocr_v2(rect=[404, 592, 778, 700],
                                                                   pattern='31') and 箱子 == 1 or 箱子 == 3 and 暂时不购买 == 1 and Ocr.mlkitocr_v2(
                                rect=[404, 592, 778, 700], pattern='31'):
                                click(586, 651)
                                time.sleep(5)
                                click(1129, 639)
                                time.sleep(5)
                                time.sleep(2)
                                if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                                    time.sleep(20)
                                    if not zi("取消", 0, 300, 422, 583, 561):
                                        购买 += 1
                                click(178, 181)
                        else:
                            暂时不购买 = 0

                        x += 90
                        time.sleep(2)
                        zi("免费", 0, 410, 306, 758, 419)

                    time.sleep(2)
                    # 0不开启  #1开启陆战 #2开启海战 #3全开

                    if 购买 < 2 and zi("5000", 0, 419, 317, 1251, 671):
                        time.sleep(2)
                        购买 += 1
                        if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                            time.sleep(20)
                            zi("取消", 0, 300, 422, 583, 561)
                        else:
                            click(447, 493)
                            time.sleep(2)
                    else:
                        action.slide(1144, 419, 699, 408)
                        time.sleep(2)
                        if zi("5000", 0, 419, 317, 1251, 671):
                            time.sleep(2)
                            if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                                time.sleep(20)
                                zi("取消", 0, 300, 422, 583, 561)
                            else:
                                click(447, 493)
                                time.sleep(2)
                    if 购买 < 2 and zi("5000", 0, 419, 317, 1251, 671):
                        time.sleep(2)
                        购买 += 1
                        if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                            time.sleep(20)
                            zi("取消", 0, 300, 422, 583, 561)
                        else:
                            click(447, 493)
                            time.sleep(2)
                    else:
                        action.slide(1144, 419, 699, 408)
                        time.sleep(2)
                        if zi("5000", 0, 419, 317, 1251, 671):
                            time.sleep(2)
                            if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                                time.sleep(20)
                                zi("取消", 0, 300, 422, 583, 561)
                            else:
                                click(447, 493)
                                time.sleep(2)
                    click(178, 181)
                    time.sleep(0.5)

                    退出()

                    # if zi("5000", 0, 419, 317, 1251, 671):
                    #     time.sleep(2)
                    #     if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                    #         time.sleep(20)
                    #         zi("取消", 0, 300, 422, 583, 561)
                    #     else:
                    #         click(447, 493)
                    #         time.sleep(2)
                    # else:
                    #     action.slide(1144, 419, 699, 408)
                    #     time.sleep(2)
                    #     if zi("5000", 0, 419, 317, 1251, 671):
                    #         time.sleep(2)
                    #         if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                    #             time.sleep(20)
                    #             zi("取消", 0, 300, 422, 583, 561)
                    #         else:
                    #             click(447, 493)
                    #             time.sleep(2)
                    切换模式(3)
                    退出()
                if 蓝图 == 1:
                    click(906, 75)
                    time.sleep(2)
                    click(240, 187)
                    time.sleep(2)
                    if Ocr.mlkitocr_v2(rect=[506, 323, 682, 402], pattern='100'):
                        time.sleep(2)
                        click(584, 366)
                        time.sleep(2)

                        actions = [
                            "click(404, 229)",
                            "click(640, 221)",
                            "click(866, 209)",
                            "click(393, 331)",
                            "click(642, 351)",
                            "click(894, 320)"
                        ]

                        # 随机选择并执行一行代码
                        random_action = random.choice(actions)
                        exec(random_action)

                        time.sleep(2)
                        click(792, 544)
                        time.sleep(2)
                        if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                            time.sleep(10)
                            click(90, 79)
                            zi("取消", 0, 300, 422, 583, 561)
                        else:
                            click(447, 493)
                            time.sleep(2)
                        退出()
                    else:
                        退出()
                if 箱子 != 0 and 暂时不购买 == 1:
                    # if 箱子 == 1:
                    #     退出()
                    #     time.sleep(4)
                    #     # 切换载具
                    #     切换模式(2)
                    #     time.sleep(4)
                    #     退出()
                    #
                    #     #点击商城
                    #     click(747, 56)
                    #     time.sleep(1.5)
                    #     click(178, 181)
                    #     time.sleep(2.5)
                    #     if Ocr.mlkitocr_v2(rect=[404, 592, 778, 700], pattern='31'):
                    #         click(586, 651)
                    #         time.sleep(5)
                    #         click(1129, 639)
                    #         time.sleep(5)
                    #         time.sleep(2)
                    #         if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                    #             time.sleep(20)
                    #             zi("取消", 0, 300, 422, 583, 561)
                    #         click(178, 181)
                    #
                    #         退出()
                    #
                    #     退出()
                    #     time.sleep(4)
                    #     # 切换载具
                    #     切换模式(1)
                    #     退出()

                    if 箱子 == 2 and 暂时不购买 == 1 or 箱子 == 3 and 暂时不购买 == 1:
                        退出()
                        time.sleep(2)
                        切换模式(2)
                        time.sleep(2)
                        退出()
                        click(747, 56)
                        time.sleep(1.5)

                        click(178, 181)
                        time.sleep(2.5)
                        if Ocr.mlkitocr_v2(rect=[404, 592, 778, 700], pattern='31'):
                            click(586, 651)
                            time.sleep(5)
                            click(1129, 639)
                            time.sleep(5)
                            time.sleep(2)
                            if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                                time.sleep(20)
                                zi("取消", 0, 300, 422, 583, 561)
                            click(178, 181)
                            退出()
                        else:
                            退出()
                    #
                    # elif 箱子 == 3:
                    # if Ocr.mlkitocr_v2(rect=[404, 592, 778, 700], pattern='31'):
                    #     click(586, 651)
                    #     time.sleep(5)
                    #     click(1129, 639)
                    #     time.sleep(5)
                    #     time.sleep(2)
                    #     meiqian = 0
                    #     if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                    #         time.sleep(20)
                    #         if zi("取消", 0, 300, 422, 583, 561):
                    #             meiqian = 1
                    #
                    #     click(178, 181)
                    #     退出()
                    #     退出()
                    #     if meiqian == 1:
                    #         time.sleep(4)
                    #         # 切换载具
                    #         切换模式(2)
                    #         退出()
                    #
                    #         # 点击商城
                    #         click(747, 56)
                    #         time.sleep(1.5)
                    #
                    #         click(178, 181)
                    #         time.sleep(2.5)
                    #         if Ocr.mlkitocr_v2(rect=[404, 592, 778, 700], pattern='31'):
                    #             click(586, 651)
                    #             time.sleep(5)
                    #             click(1129, 639)
                    #             time.sleep(5)
                    #             time.sleep(2)
                    #             if tu("购买", 0, 1, 1, 673, 413, 988, 549, 1):
                    #                 time.sleep(20)
                    #                 zi("取消", 0, 300, 422, 583, 561)
                    #             click(178, 181)
                    #             退出()
                    #
                    #         退出()
                    #         time.sleep(4)
                    #         # 切换载具
                    #         切换模式(1)
                    #         退出()


                # 0不开启  #1开启陆战 #2开启海战 #3全开

                else:
                    pass
                if 加入战斗():
                    time.sleep(2)
                else:
                    退出()
            if True:
                addaddxx = 0
                qerrq = 1
                time.sleep(2)
                click(99, 419)

                time.sleep(2)
                click(212, 138)
                time.sleep(0.5)
                click(628, 136)
                affaww = 0
                time.sleep(3)
                nima1 = 0
                bb == 1
                ssguang = 0
                kanchi = 0
                wwwwc = 0
                网络问题局部 = 0
                重启过 = 0
                切换加速 = 0
                网络问题 = 0
                renwuwancheng = 0
            while qerrq == 1:

                if stop_event.is_set():
                    pass
                if 闪退() or 重启过 == 1:
                    pass

                if 加入战斗():
                    click(104, 415)
                    time.sleep(2)
                    click(209, 145)
                    time.sleep(2)

                else:
                    time.sleep(5)

                if tu("任务", 0, 1, 1, 1025, 263, 1220, 476, 1, 0.8):
                    time.sleep(4)
                    click(1166, 206)
                    time.sleep(2)

                    if addaddxx >= 50:
                        qerrq += 1
                    else:
                        addaddxx += 1
                else:
                    # if Ocr.mlkitocr_v2(rect=[370, 272, 492, 609], pattern='陆战') and not Ocr.paddleocr_v2(rect =[1058,503,1183,573],pattern = '已获得'):
                    #    res = Ocr.mlkitocr_v2(rect=[370, 272, 492, 609], pattern='陆战')
                    #     nima1 += 1
                    #  if res:
                    #      # 循环打印识别到的每一个段落
                    #      for r in res:
                    #          if click(1118, r.center_y) and Ocr.mlkitocr_v2(rect=[1019, 325, 1220, 674],
                    #                                                         pattern='进度'):
                    if renwuwancheng == 0 and FindColors.find("1121,525,#3CC58A|1130,524,#3BBF85|1083,535,#FFFFFF",
                                                              rect=[1043, 270, 1213, 693]) and not Ocr.mlkitocr_v2(
                            rect=[1039, 469, 1215, 584], pattern='已') and not zi("RE", 0, 934,230,1234,704, 1):
                        point = FindColors.find("1121,525,#3CC58A|1130,524,#3BBF85|1083,535,#FFFFFF",
                                                rect=[1043, 270, 1213, 693])
                        if point:
                            # 打印 x坐标 和 y坐标
                            if click(point.x, point.y) and not Ocr.paddleocr_v2(rect=[1058, 503, 1183, 573],
                                                                                pattern='已获得') and affaww == 0:
                                log("可以观看")
                                time.sleep(2)
                                tt = 1
                                while tt == 1:
                                    if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                                        click(640, 524)
                                    time.sleep(3)
                                    if stop_event.is_set():
                                        return
                                    if 闪退() or 重启过 == 1:
                                        return
                                    if Selector().type("WebView").find():
                                        break
                                    if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                                        time.sleep(5)
                                        网络问题局部 += 1
                                        if Selector().type("WebView").find():
                                            break
                                    else:
                                        if Selector().type("WebView").find():
                                            break
                                        click(point.x, point.y)
                                    if Selector().type("WebView").find():
                                        break
                                    if click(point.x, point.y):
                                        tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                                        time.sleep(2)
                                        if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                                            网络问题 += 1
                                            网络问题局部 += 1
                                    if 服务器():
                                        网络问题局部 += 1
                                    if 网络问题局部 >= 15:
                                        切换加速器()
                                        切换加速 += 1
                                        time.sleep(3)
                                    if Selector().type("WebView").find():
                                        break

                                if Selector().type("WebView").find():
                                    log("等待跳过广告")

                                    广告及收益(0)
                        #     else:
                        #         click(1166, 206)
                        #         time.sleep(0.5)
                        #         click(1053, 206)
                        #         time.sleep(0.5)
                        #         click(906, 204)
                        #         time.sleep(0.5)
                        #         click(784, 204)
                        #         time.sleep(0.5)
                        #         click(648, 204)
                        #         time.sleep(0.5)
                        #         time.sleep(1)
                        #         # 周任务
                        #         click(968, 133)
                        #         time.sleep(1)
                        #         affaww += 0.5
                        #         if affaww == 1:
                        #             qerrq += 1
                        #
                        # else:
                        #     click(1166, 206)
                        #     time.sleep(0.5)
                        #     click(1053, 206)
                        #     time.sleep(0.5)
                        #     click(906, 204)
                        #     time.sleep(0.5)
                        #     click(784, 204)
                        #     time.sleep(0.5)
                        #     click(648, 204)
                        #     time.sleep(0.5)
                        #     time.sleep(1)
                        #     # 周任务
                        #     click(968, 133)
                        #     time.sleep(1)
                        #     affaww += 0.5
                        #     if affaww == 1:
                        #         qerrq += 1
                    else:
                        renwuwancheng = 1
                        click(1166, 206)
                        time.sleep(0.5)
                        click(1053, 206)
                        time.sleep(0.5)
                        click(906, 204)
                        time.sleep(0.5)
                        click(784, 204)
                        time.sleep(0.5)
                        click(648, 204)
                        time.sleep(0.5)
                        time.sleep(1)
                        # 周任务
                        click(968, 133)
                        time.sleep(1)
                        affaww += 0.5
                        if affaww == 1:
                            qerrq += 1

            退出()
    程度=0
    def 赛季1():
        global xa, 网络问题, 赛季任务,程度
        if 加入战斗():
            time.sleep(2)
        else:
            退出()
        click(99, 416)
        time.sleep(2)
        click(224,312)
        time.sleep(2)
        click(440,131)
        xa = 447
        完成程度 = 0
        while True:
            if Ocr.mlkitocr_v2(rect=[1025, 246, 1234, 651], pattern='进行游戏') and not tu("任务", 0, 1, 1,1025,169,1219,270,1,0.7) or zi("RE", 1, 1032,271,1215,701, 1)and not tu("任务", 0, 1, 1,1025,169,1219,270,1,0.7):
                time.sleep(2)
                break
            if tu("任务", 0, 1, 1,1025,169,1219,270,1,0.7):
                time.sleep(1.5)
                if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                    click(640, 524)
                time.sleep(2)
                continue

            time.sleep(1.5)
            if not Ocr.mlkitocr_v2(rect =[365,100,1229,159],pattern = '日'):
                tu("2", 0, 1, 1, 24, 0, 145, 134, 0)
            if Ocr.mlkitocr_v2(rect =[1005,178,1230,266],pattern = '已') and Ocr.mlkitocr_v2(rect =[365,100,1229,159],pattern = '日') or FindColors.find("1110,221,#AEAEAE|1118,225,#656565|1142,229,#6E6E6E|1144,231,#6F6F6F|1064,209,#7A7A7A",rect=[1027,170,1230,296]) and Ocr.mlkitocr_v2(rect =[365,100,1229,159],pattern = '日')  and Ocr.mlkitocr_v2(rect =[1049,277,1208,370],pattern = '已'):
                if not FindColors.find("1164,348,#33C284", rect=[1019, 173, 1211, 579]):
                    xa += 170
                    click(xa, 127)
                    完成程度 += 1
                    log("完成")

                    if 完成程度 > 程度:
                        程度 += 1
                        email_song(f'{用户邮箱},{设备号}活动任务反馈',
                                   f'"活动任务"已经完成 {完成程度}份,共5份',
                                   f'{报告邮箱}', 4)
                        email_song('活动任务反馈',
                                   f'"活动任务"已经完成 {完成程度}份,共5份',
                                   f'{用户邮箱}', 4)
                        if 程度 >= 5:
                            程度 = 0
                    if xa > 1127:
                        赛季任务 = 0
                        break
                    continue

            if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                click(640, 524)
            if not Ocr.mlkitocr_v2(rect =[365,100,1229,159],pattern = '日'):
                if 加入战斗():
                    time.sleep(2)
                else:
                    退出()
                click(99, 416)
                time.sleep(2)
                click(224, 312)
                time.sleep(2)
                click(440, 131)

            if stop_event.is_set():
                return
            # if not Ocr.mlkitocr_v2(rect=[1010, 260, 1229, 683], pattern='增加进度') and not Ocr.mlkitocr_v2(
            #         rect=[1010, 260, 1229, 683], pattern='进行游戏'):
            #     xa += 170
            #     click(xa, 226)
            #     完成程度 += 1
            #
            #     continue
            if zi("获得", 0, 996, 263, 1229, 481):
                click(xa, 226)

            time.sleep(3)

            if zi("增加进度", 0, 996, 263, 1229, 481):
                time.sleep(10)
                tt = 1
                bb == 1
                ssguang = 0
                kanchi = 0
                wwwwc = 0
                网络问题局部 = 0
                重启过 = 0
                切换加速 = 0
                while tt == 1:
                    if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                        click(640, 524)
                    time.sleep(3)
                    if stop_event.is_set():
                        return
                    if 闪退() or 重启过 == 1:
                        return
                    if Selector().type("WebView").find():
                        break
                    if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                        time.sleep(5)
                        网络问题局部 += 1
                        if Selector().type("WebView").find():
                            break
                    else:
                        if Selector().type("WebView").find():
                            break
                        zi("增加进度", 0, 996, 263, 1229, 481)
                    if Selector().type("WebView").find():
                        break
                    if zi("增加进度", 0, 996, 263, 1229, 481):
                        tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                        time.sleep(2)
                        if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                            网络问题 += 1
                            网络问题局部 += 1
                    if 服务器():
                        网络问题局部 += 1
                    if 网络问题局部 >= 3:
                        切换加速器()
                        切换加速 += 1
                        time.sleep(3)
                        去宝箱界面()
                        网络问题局部 = 5
                        if 切换加速 == 2:
                            重启()
                        continue
                    if Selector().type("WebView").find():
                        break
                    if Selector().type("WebView").find():
                        log("等待跳过广告")

                        广告及收益(0)
                        time.sleep(1.5)
                        if not Ocr.mlkitocr_v2(rect=[365, 100, 1229, 159], pattern='日'):
                            tu("2", 0, 1, 1, 24, 0, 145, 134, 0)
            if Selector().type("WebView").find():
                    log("等待跳过广告")

                    广告及收益(0)
                    time.sleep(1.5)
                    if not Ocr.mlkitocr_v2(rect=[365, 100, 1229, 159], pattern='日'):
                        tu("2", 0, 1, 1, 24, 0, 145, 134, 0)
            if Ocr.mlkitocr_v2(rect=[1025, 246, 1234, 651], pattern='进行游戏') and not tu("任务", 0, 1, 1,1025,169,1219,270,1,0.7):
                time.sleep(2)
                break
            time.sleep(2)
            if not Ocr.mlkitocr_v2(
                    rect=[1049, 277, 1208, 370], pattern='已'):
                tu("2", 0, 1, 1, 24, 0, 145, 134, 0)
                time.sleep(3)
            if Ocr.mlkitocr_v2(rect=[1061, 165, 1209, 258], pattern='已') and Ocr.mlkitocr_v2(
                    rect=[365, 100, 1229, 159], pattern='日') or FindColors.find(
                    "1110,221,#AEAEAE|1118,225,#656565|1142,229,#6E6E6E|1144,231,#6F6F6F|1064,209,#7A7A7A",
                    rect=[1027, 170, 1230, 296]) and Ocr.mlkitocr_v2(rect=[365, 100, 1229, 159],
                                                                     pattern='日') and Ocr.mlkitocr_v2(
                    rect=[1049, 277, 1208, 370], pattern='已'):

                if not FindColors.find("1164,348,#33C284", rect=[1019, 173, 1211, 579]):
                    xa += 170
                    click(xa, 127)
                    完成程度 += 1
                    log("完成")

                    if 完成程度 > 程度:
                        程度 += 1
                        email_song(f'{用户邮箱},{设备号}活动任务反馈',
                                   f'"活动任务"已经完成 {完成程度}份,共5份',
                                   f'{报告邮箱}', 4)
                        email_song('活动任务反馈',
                                   f'"活动任务"已经完成 {完成程度}份,共5份',
                                   f'{用户邮箱}', 4)
                        if 程度 >= 5:
                            程度 = 0

                    if xa > 1127:
                        赛季任务 = 0
                        break
                    continue

    def 赛季():
        global xa, 网络问题, 赛季任务, 程度
        if 加入战斗():
            time.sleep(2)
        else:
            退出()
        click(99, 416)
        time.sleep(2)
        click(232, 240)
        time.sleep(2)
        click(447, 226)
        xa = 447
        完成程度 = 0
        while True:
            if zi("获得",0,1030,258,1222,379,1):
                pass
            time.sleep(1.5)
            if not Ocr.mlkitocr_v2(rect=[574, 72, 695, 201], pattern='200'):
                if 加入战斗():
                    time.sleep(2)
                else:
                    退出()
                click(99, 416)
                time.sleep(2)
                click(232, 240)
                time.sleep(2)
                click(447, 226)

            if stop_event.is_set():
                return
            if not Ocr.mlkitocr_v2(rect=[1010, 260, 1229, 683], pattern='增加进度') and not Ocr.mlkitocr_v2(
                    rect=[1010, 260, 1229, 683], pattern='进行游戏') and Ocr.mlkitocr_v2(rect=[574, 72, 695, 201],
                                                                                         pattern='200') or Ocr.mlkitocr_v2(rect =[587,425,1076,552],pattern = '开放'):

                if Ocr.mlkitocr_v2(rect =[587,425,1076,552],pattern = '开放'):
                    email_song(f'{用户邮箱},{设备号}赛季任务反馈',
                               f'"赛季任务"已经完成 ',
                               f'{报告邮箱}', 4)
                    email_song('赛季任务反馈',
                               f'"赛季任务"已经完成',
                               f'{用户邮箱}', 4)
                    赛季任务 = 0

                    return
                xa += 170
                click(xa, 226)
                完成程度 += 1

                if 完成程度 > 程度:
                    程度 += 1
                    email_song(f'{用户邮箱},{设备号}赛季任务反馈',
                               f'"赛季任务"已经完成 {完成程度}份,共5份',
                               f'{报告邮箱}', 4)
                    email_song('赛季任务反馈',
                               f'"赛季任务"已经完成 {完成程度}份,共5份',
                               f'{用户邮箱}', 4)
                    if 程度>=5:
                        程度=0
                if xa > 1127:
                    赛季任务 = 0
                    break
                continue
            if zi("获得", 0, 996, 263, 1229, 481):
                click(xa, 226)

            time.sleep(3)
            # if not FindColors.find("1145,520,#3DC188|1154,520,#3EC68B",rect=[1021,277,1230,695]) and not zi("进行游戏",1,1021,277,1230,695,1):
            #     pass
            if zi("增加进度", 0, 996, 263, 1229, 481):
                time.sleep(10)
                tt = 1
                bb == 1
                ssguang = 0
                kanchi = 0
                wwwwc = 0
                网络问题局部 = 0
                重启过 = 0
                切换加速 = 0
                while tt == 1:
                    if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                        click(640, 524)
                    time.sleep(3)
                    if stop_event.is_set():
                        return
                    if 闪退() or 重启过 == 1:
                        return
                    if Selector().type("WebView").find():
                        break
                    if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                        time.sleep(5)
                        网络问题局部 += 1
                        if Selector().type("WebView").find():
                            break
                    else:
                        if Selector().type("WebView").find():
                            break
                        zi("增加进度", 0, 996, 263, 1229, 481)
                    if Selector().type("WebView").find():
                        break
                    if zi("增加进度", 0, 996, 263, 1229, 481):
                        tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                        time.sleep(2)
                        if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                            网络问题 += 1
                            网络问题局部 += 1
                    if 服务器():
                        网络问题局部 += 1
                    if 网络问题局部 >= 3:
                        切换加速器()
                        切换加速 += 1
                        time.sleep(3)
                        去宝箱界面()
                        if 切换加速 == 6:
                            重启()
                            切换加速=0
                        continue
                    if Selector().type("WebView").find():
                        break
                if Selector().type("WebView").find():
                    log("等待跳过广告")

                    广告及收益(0)

                    log("跳过广告成功")

            if Selector().type("WebView").find():
                log("等待跳过广告")

                广告及收益(0)

                log("跳过广告成功")

            if Ocr.mlkitocr_v2(rect=[1025, 246, 1234, 651], pattern='进行游戏'):
                time.sleep(2)
                break
            time.sleep(2)

            if not Ocr.mlkitocr_v2(rect=[574, 72, 695, 201], pattern='200'):
                tu("2", 0, 1, 1, 24, 0, 145, 134, 0)
                time.sleep(3)
            if not Ocr.mlkitocr_v2(rect=[1010, 260, 1229, 683], pattern='增加进度') and not Ocr.mlkitocr_v2(
                    rect=[1010, 260, 1229, 683], pattern='进行游戏') and Ocr.mlkitocr_v2(rect=[574, 72, 695, 201],
                                                                                         pattern='200') or Ocr.mlkitocr_v2(rect =[587,425,1076,552],pattern = '开放'):

                if Ocr.mlkitocr_v2(rect=[587, 425, 1076, 552], pattern='开放'):
                    email_song(f'{用户邮箱},{设备号}赛季任务反馈',
                               f'"赛季任务"已经完成 ',
                               f'{报告邮箱}', 4)
                    email_song('赛季任务反馈',
                               f'"赛季任务"已经完成',
                               f'{用户邮箱}', 4)
                    赛季任务 = 0
                    return
                xa += 170
                click(xa, 226)
                完成程度 += 1
                if 完成程度 > 程度:
                    程度 += 1
                    email_song(f'{用户邮箱},{设备号}赛季任务反馈',
                               f'"赛季任务"已经完成 {完成程度}份,共5份',
                               f'{报告邮箱}', 4)
                    email_song('赛季任务反馈',
                               f'"赛季任务"已经完成 {完成程度}份,共5份',
                               f'{用户邮箱}', 4)
                    if 程度>=5:
                        程度=0
                if xa > 1127:
                    赛季任务 = 0
                    break
                continue
    def 执行函数(func, timeout):
        """在独立线程中执行指定的函数，并在超时后终止线程"""

        class ThreadWithTimeout(threading.Thread):
            def __init__(self, target, timeout):
                super().__init__(target=target)
                self._timeout = timeout
                self._start_time = None
                self._completed = threading.Event()

            def run(self):
                self._start_time = time.time()
                super().run()
                self._completed.set()  # 标记线程完成

            def has_timed_out(self):
                return time.time() - self._start_time >= self._timeout

            def kill(self):
                # 获取当前线程的ID
                thread_id = ctypes.c_long(self.ident)
                # 调用底层API强制终止线程
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
                if res == 0:
                    raise ValueError("线程ID无效")
                elif res > 1:
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                    raise SystemError("强制终止线程失败")

        if not stop_event.is_set():
            log(f"函数 {func.__name__} 开始执行")
            thread = ThreadWithTimeout(target=func, timeout=timeout)
            thread.start()
        else:
            return

        # 等待指定时间
        thread.join(timeout)

        if thread.is_alive():
            log(f"函数 {func.__name__} 超时，将执行重启操作")

            # 强制终止线程
            thread.kill()
            记录暂停()
            重启()
            计算并更新()
            return True
        else:
            if thread.has_timed_out():
                log(f"函数 {func.__name__} 超时，将执行重启操作")
                记录暂停()
                重启()
                计算并更新()
                return True
            else:
                log(f"函数 {func.__name__} 执行完成")
                return False


    def 检查日期变化并执行任务():
        global daynow1

        now = datetime.now()

        dayold = now.day
        if dayold != daynow1:
            切换模式(1)
            退出()
            daynow1 = dayold
            任务()
    def 检查时间执行广告():
        global daynow2, 网络问题局部, 切换加速, kanchi

        now = datetime.now()
        网络问题局部=0
        hournow1 = now.day
        if hournow1 -daynow2>=2:
            daynow2 = hournow1
            log("开始每日任务")
            if 加入战斗():
                time.sleep(2)
            else:
                退出()
                zi("取消", 0, 322, 439, 563, 549)
                time.sleep(2)
                if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern='稍后'):
                    time.sleep(4)
                    click(815, 649)
                    time.sleep(3)
                    退出()
            log("开始买东西")
            click(1039, 73)
            time.sleep(1.5)
            if not zi("金", 0, 57, 128, 400, 695, 1):
                click(221, 183)
            time.sleep(1.5)
            if zi("免费", 0, 410, 306, 758, 419):
                time.sleep(2)
            if True:
                zi("观看", 0, 422, 337, 748, 413, 1)
                tt = 1
                if Ocr.mlkitocr_v2(pattern='已领取该奖励。'):
                    time.sleep(1)
                    click(687, 479)
                    return
                while tt == 1:
                    if Ocr.mlkitocr_v2(pattern = '已领取该奖励。'):
                        time.sleep(1)
                        click(687, 479)
                        return
                    if not zi("观看", 0, 422, 337, 748, 413, 1) and not tu("2", 1, 1, 1, 24, 0, 145, 134, 0, 0.8, 1) or tu("2", 1, 1, 1, 24, 0, 145, 134, 1,
                                                                                   0.8, 1) and not zi("观看", 0, 422, 337, 748, 413, 1) :
                        if 加入战斗():
                            time.sleep(2)
                        else:
                            退出()
                            zi("取消", 0, 322, 439, 563, 549)
                            time.sleep(2)
                            if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern='稍后'):
                                time.sleep(4)
                                click(815, 649)
                                time.sleep(3)
                                退出()
                        log("开始买东西")
                        click(1039, 73)
                        time.sleep(1.5)
                        if not zi("金", 0, 57, 128, 400, 695, 1):
                            click(221, 183)
                        time.sleep(1.5)
                        if zi("免费", 0, 410, 306, 758, 419):
                            time.sleep(2)
                    if Ocr.mlkitocr_v2(pattern = '已领取该奖励。'):
                        time.sleep(1)
                        click(687, 479)
                        return
                    if Selector().type("WebView").find():
                        break
                    if FindImages.find_all_template([R.img("已获得1.png"), ], confidence=0.90):
                        click(640, 524)
                    time.sleep(3)
                    if stop_event.is_set():
                        return
                    if 闪退() or 重启过 == 1:
                        return
                    if Selector().type("WebView").find():
                        break
                    if tu("正在加载", 1, 1, 1, 452, 179, 902, 348, 0, 0.7):
                        time.sleep(5)
                        网络问题局部 += 1
                        if Selector().type("WebView").find():
                            break
                    else:
                        if Selector().type("WebView").find():
                            break

                        if zi("观看", 0, 422, 337, 748, 413, 1):
                            zi("观看", 0, 422, 337, 748, 413, 1)
                    if Ocr.mlkitocr_v2(pattern = '已领取该奖励。'):
                        time.sleep(1)
                        click(687, 479)
                        return
                    if Selector().type("WebView").find():
                        break
                    if zi("观看", 1, 422, 337, 748, 413, 1):
                        tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609, 1)
                        time.sleep(2)
                        if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                            网络问题局部 += 1
                    if 服务器():
                        网络问题局部 += 1
                    if 网络问题局部 >= 3:
                        切换加速 += 1
                        网络问题局部 = 0
                        if 切换加速 == 10:
                            重启()
                            去宝箱界面()
                            切换加速器()
                            continue
                        切换加速器()

                        time.sleep(3)
                        continue

                    if Selector().type("WebView").find():
                        break
                    if Ocr.mlkitocr_v2(rect=[701, 610, 945, 683], pattern='进行游戏'):
                        return
                log("未出现问题")
                if Selector().type("WebView").find():
                    广告及收益(2)
                    网络问题局部 = 0
        else:
            return False

if "寻找攻击":
    def 开炮():
        global 游戏结束
        log("开炮")
        if 模型("敌船", 0):
            瞄准(识别x, 识别y + 10)
            time.sleep(1.5)
        if kekai==0:
            time.sleep(0.4)
            click(1052,511)
            time.sleep(0.4)
            click(986,563)
            time.sleep(0.4)
            click(997,434)
            time.sleep(0.4)
            click(1052,621)
            time.sleep(0.4)
            click(1112,557)
            time.sleep(0.4)
            click(1112,436)
        # else:
        #     if stop_event.is_set():
        #         return
        #     if zi("返回基地", 0, 19, 561, 348, 711, 1) or zi("返回港口", 0, 19, 561, 348, 711, 1):
        #         pass
        #     if zi("返回港口", 0, 445, 575, 898, 713, 1) or zi("返回基地", 0, 19, 561, 348, 711, 1):
        #         if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
        #                 rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
        #                                                                            pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
        #             rect=[1027, 0, 1124, 45], pattern='PL'):
        #             pass
        #         if Ocr.mlkitocr_v2(rect=[580, 629, 705, 683], pattern='返回港口'):
        #             pass
        #
        #             click(634, 654)
        #             time.sleep(6)
        #         if zi('返回港口', 0, 569, 620, 719, 697, 1):
        #             pass
        #
        #         if Ocr.mlkitocr_v2(rect=[983, 614, 1206, 683], pattern='跳过'):
        #             pass
        #             click(1121, 643)
        #             time.sleep(2)
        #
        #         if zi("返回港口", 0, 67, 615, 303, 685, 1) or Ocr.mlkitocr_v2(
        #                 rect=[67, 615, 303, 685],
        #                 pattern='升级舰艇'):
        #             pass
        #
        #             time.sleep(0.5)
        #
        #             click(180, 649)
        #             time.sleep(4)
        #         if 游戏结束 == 1:
        #             if zi('获得', 0, 940, 583, 1237, 717, 1):
        #                 time.sleep(5)
        #                 zi('购买', 0, 59, 345, 654, 717)
        #                 time.sleep(5)
        #                 zi('购买', 0, 724, 433, 991, 555)
        #                 time.sleep(3)
        #                 zi('取消', 0, 308, 453, 580, 547)
        #                 time.sleep(3)
        #                 退出()
        #                 time.sleep(5)
        #                 if zi("稍后", 0, 662, 592, 937, 708):
        #                     time.sleep(5)
        #                     退出()


    x_保存坐标 = []
    y_保存坐标 = []
    保存移动长度 = []


    def 保存到组(x, y, 移动长度):

        x_保存坐标.append(x)
        y_保存坐标.append(y)
        保存移动长度.append(移动长度)
        return


    def 瞄准(x, y, z=20, 移动长度=150, x1=635, y1=335, speed=2.5):
        random_offset = random.randint(0, z)
        # 将随机值加到y1上
        y1 -= random_offset
        # 准星358
        zzx = x1
        zzy = y1
        反x = x1 - x + x1
        反y = y1 - y + y1

        # 计算目标点与当前位置的距离
        xxc = x - zzx
        yyc = y - zzy

        distance = math.sqrt(xxc ** 2 + yyc ** 2)  # distance = math.sqrt((xxc) ** 2 + (yyc) ** 2)
        # log(f"距离: {distance}")

        # 根据距离计算移动时间
        move_time = distance / speed
        # log(f"移动时间: {move_time}")
        if move_time <= 150:
            move_time = 150
        if move_time >= 200:
            move_time = 200
        # 调用action.slide函数进行移动
        保存到组(反x, 反y, 移动长度)
        action.slide(zzx, zzy, x, y, 移动长度)


    def 视角回正(x, y, 移动长度=150, x1=635, y1=335, speed=2.5):
        # 准星358
        zzx = x1
        zzy = y1

        # 计算目标点与当前位置的距离
        xxc = x - zzx
        yyc = y - zzy

        distance = math.sqrt(xxc ** 2 + yyc ** 2)  # distance = math.sqrt((xxc) ** 2 + (yyc) ** 2)
        # log(f"距离: {distance}")

        # 根据距离计算移动时间
        move_time = distance / speed
        # log(f"移动时间: {move_time}")
        if move_time <= 150:
            move_time = 150
        if move_time >= 200:
            move_time = 200
        action.slide(zzx, zzy, x, y, 移动长度)


    def 复位():
        while len(x_保存坐标) > 0:
            x = x_保存坐标.pop(0)
            y = y_保存坐标.pop(0)
            移动长度 = 保存移动长度.pop(0)
            视角回正(x, y, 移动长度)
            time.sleep(1)


    def 寻找目标(x, y, x1, y1, z=40):
        if FindColors.find("580,316,#F76D67", rect=[x, y, x1, y1]):
            try:
                # log("进一步搜索目标")
                hong = FindColors.find("580,316,#F76D67", rect=[x, y, x1, y1])
                瞄准(hong.x, hong.y, z)
                return True
            except AttributeError:
                # log("未找到目标")
                time.sleep(1.5)
                return True
        else:
            # log("未找到目标")
            time.sleep(1.5)
            return False


    def 确认目标(x, y, x1, y1):
        if FindColors.find("580,316,#F76D67", rect=[x, y, x1, y1]):
            # log("目标在范围内")
            time.sleep(1.5)
            return True
        else:
            # log("未找到目标")
            time.sleep(1.5)
            return False

if "战斗部分":

    def 返回港口(x=0):
        global 游戏结束
        if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                           pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL'):
            游戏结束 = 1
            return True

        退出()
        if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                           pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL'):
            游戏结束 = 1
            return True
        else:
            if zi('获得', 0, 940, 583, 1237, 717, 1) or zi('获取', 0, 940, 583, 1237, 717, 1):
                time.sleep(5)
                zi('购买', 0, 59, 345, 654, 717)
                time.sleep(5)
                zi('购买', 0, 724, 433, 991, 555)
                time.sleep(3)
                zi('取消', 0, 308, 453, 580, 547)
                time.sleep(3)
                退出()
                time.sleep(5)
                if zi("稍后", 0, 662, 592, 937, 708):
                    time.sleep(5)
                    退出()

                if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                        rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                                   pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL'):
                    游戏结束 = 1
                    return True
            else:
                if Ocr.mlkitocr_v2(rect=[983, 614, 1206, 683], pattern='获取'):
                    游戏结束 = 1
                    time.sleep(0.5)
                    if x != 0:
                        click(180, 649)
                    time.sleep(5)
                    if Ocr.mlkitocr_v2(rect=[521, 575, 750, 654], pattern='获得'):
                        time.sleep(0.5)
                        click(642, 617)
                        time.sleep(4)
                        click(798, 640)
                        退出()

                        if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90],
                                           pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                            rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                                       pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                            rect=[1027, 0, 1124, 45], pattern='PL'):
                            return True

        return False


    def 游戏返回主页():
        global apox
        # 是否有
        if not FindColors.find("899,627,#2790A4"):
            if not 加入战斗() and not 返回港口():
                click(643, 658)

            time.sleep(4)

            if 返回港口(1) and not FindColors.find("899,627,#2790A4") and not Ocr.mlkitocr_v2(rect=[67, 615, 303, 685],
                                                                                              pattern='返回港口'):
                if 返回港口(1):
                    pass

            if 返回港口(1):
                if 返回港口(1):
                    pass

            if True and not 返回港口(1) and not FindColors.find("899,627,#2790A4"):
                退出()
                return True

        return False


    def 加入战斗(x=0):
        time.sleep(0.25)
        if zi("加入战斗", 1, 795, 515, 1271, 705, 1):
            if x != 0:
                zi("加入战斗", 0, 795, 515, 1271, 705, 1)
                return True
            return True
        else:
            if FindColors.find("1142,624,#CC1208|1019,618,#D31208|1093,622,#CE1208|1085,647,#FFFFFF",
                               rect=[328, 113, 1254, 705]):
                if x != 0:
                    point = FindColors.find("1142,624,#CC1208|1019,618,#D31208|1093,622,#CE1208|1085,647,#FFFFFF",
                                            rect=[328, 113, 1254, 705])
                    if point:
                        # 打印 x坐标 和 y坐标
                        click(point.x, point.y)
                    return True
                return True
            else:
                if zi("加入战斗", 1, 795, 515, 1271, 705, 1):
                    if x != 0:
                        zi("加入战斗", 0, 795, 515, 1271, 705, 1)
                        return True
                    return True
                else:
                    if zi("加入战斗", 1, 303, 144, 1268, 714, 1):
                        if x != 0:
                            zi("加入战斗", 0, 303, 144, 1268, 714, 1)
                            return True
                        return True

            return False


    def 开始进游戏空():
        开始进游戏(1)


    def 开始进游戏(x=0):
        global 重启过, 正在匹配游戏
        log("退出")
        退出()
        time.sleep(1)
        if 加入战斗(1):
            time.sleep(2)
            if 加入战斗(1):
                time.sleep(2)
        aa = 1
        bbc = 0
        afffff=0
        重启过 = 0
        正在匹配游戏 = 1
        while aa == 1:
            # if 返回港口(1):
            #     pass
            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
            res = Ocr.mlkitocr_v2(rect=[345, 280, 1240, 697], pattern='加入战斗')
            if res:
                for r in res:
                    click(r.center_x, r.center_y)
            退出()
            time.sleep(1)
            if Ocr.mlkitocr_v2(rect =[472,19,802,96],pattern = '正在加入'):
                afffff+=1
                if afffff>5:
                    click(1109,645)
                    切换加速器()
                    afffff=0
            if 服务器():
                切换加速器()
            if 加入战斗(1):
                pass
            if 服务器() and  tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
                切换加速器()

            tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609)
            time.sleep(2)
            tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0)
            if 加入战斗(1):
                time.sleep(1)
                if 加入战斗(1):
                    time.sleep(1)
            if Ocr.mlkitocr_v2(rect=[311, 144, 1061, 564], pattern='连接丟失'):
                click(645, 496)
                切换加速器()
            if FindColors.find("1080,20,#FF5D5D",rect=[837,8,1167,30]) and Ocr.mlkitocr_v2(rect =[576,629,719,695],pattern = '返回'):
                切换加速器()
            if x == 1:
                if  FindColors.find("984,407,#53BCCA",
                                                                            rect=[31, 358, 1235,
                                                                                         709]) and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
                                                                                                        709]) and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("机枪.png"), ],
                                                                                            rect=[31, 235, 1265, 708],
                                                                                            confidence=0.95) and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("炸弹.png"), ],
                                                                                            rect=[11, 365, 1274, 717],
                                                                                            confidence=0.95) and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL'):
                    正在匹配游戏 == 0
                    log("进入游戏成功")
                    break
            else:
                if Ocr.mlkitocr_v2(rect =[516,541,950,717],pattern = '10') and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
                                                confidence=0.90) and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("984,407,#53BCCA",
                                                                               rect=[31, 358, 1235,
                                                                                     709]) and Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
                                                                                                        709]):
                    正在匹配游戏 == 0
                    log("进入游戏成功")
                    break
        # aa = 1
        # while aa == 1 and x==1:
        #     # if 返回港口(1):
        #     #     pass
        #     if stop_event.is_set():
        #         return
        #     if 闪退() or 重启过 == 1:
        #         return
        #     res = Ocr.mlkitocr_v2(rect=[345, 280, 1240, 697], pattern='加入战斗')
        #     if res:
        #         for r in res:
        #             click(r.center_x, r.center_y)
        #     退出()
        #     time.sleep(3)
        #     if 加入战斗(1):
        #         tu("取消蓝", 0, 1, 1, 271, 365, 1013, 609)
        #         time.sleep(2)
        #         if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
        #             切换加速器()
        #     if tu("确认1", 0, 1, 1, 468, 407, 1002, 639, 0):
        #         pass
        #     if 服务器():
        #         加入战斗(1)
        #         time.sleep(3)
        #     if 加入战斗(1):
        #         time.sleep(3)
        #         if 加入战斗(1):
        #             time.sleep(3)
        #     if Ocr.mlkitocr_v2(rect=[311, 144, 1061, 564], pattern='连接丟失'):
        #         click(645, 496)
        #         切换加速器()

            # if x == 1:
            #     if Ocr.mlkitocr_v2(
            #             rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("984,407,#53BCCA",
            #                                                                        rect=[31, 358, 1235,
            #                                                                              709]) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
            #                                                                                             709]) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
            #                                                                                             709]) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("机枪.png"), ],
            #                                                                                 rect=[31, 235, 1265, 708],
            #                                                                                 confidence=0.95) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("机枪.png"), ],
            #                                                                                 rect=[31, 235, 1265, 708],
            #                                                                                 confidence=0.95) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("炸弹.png"), ],
            #                                                                                 rect=[11, 365, 1274, 717],
            #                                                                                 confidence=0.95) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL'):
            #         正在匹配游戏 == 0
            #         log("进入游戏成功")
            #         if 加入战斗(1):
            #             continue
            #         else:
            #             return
            #     else:
            #         bbc += 1
            #     if bbc > 100:
            #         重启()
            #         continue
            # else:
            #     if FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
            #                                     confidence=0.90) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("984,407,#53BCCA",
            #                                                                    rect=[31, 358, 1235,
            #                                                                          709]) and Ocr.mlkitocr_v2(
            #         rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
            #                                                                                             709]):
            #         正在匹配游戏 == 0
            #         log("进入游戏成功")
            #         if 加入战斗(1):
            #             continue
            #         else:
            #             return
            #     else:
            #         bbc += 1
            #     if bbc > 100:
            #         重启()
            #         continue


    def 结束游戏():
        global 游戏结束, sssj
        sssj = 1
        游戏结束 = 0
        while sssj == 1 and 游戏结束 == 0:
            if stop_event.is_set():
                return
            # if 游戏结束 == 0 and FindColors.find("580,316,#F76D67", rect=[158, 99, 1195, 657]):
            # if FindColors.find("580,316,#F76D67", rect=[158, 99, 1195, 657]) and 游戏结束 == 0:
            # if 模型("在目标附近", 1):
            #     开炮()
            time.sleep(3)
            if 返回港口(1):
                sssj += 1
            # if not FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
            #                                     confidence=0.90) or not FindColors.find("899,627,#2790A4"):
            #     游戏结束 = 1


    def 开炮线程():
        global 游戏结束
        sssj = 1
        游戏结束 = 0
        while sssj == 1 and 游戏结束 == 0:
            if stop_event.is_set():
                return
            if 模型("在目标附近", 1):
                开炮()
            time.sleep(1)
            # if not FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
            #
            # if not FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
            #
    def 跳过():
        global 游戏结束
        sssj1 = 1
        while sssj1 == 1:
            if stop_event.is_set():
                return
            if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                               pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                rect=[1027, 0, 1124, 45], pattern='PL'):
                return
            退出()
            if zi("回", 0, 19, 561, 348, 711, 1) or zi("回", 0, 19, 561, 348, 711, 1):
                游戏结束 = 1
            if zi("回", 0, 445, 575, 898, 713, 1) or zi("回", 0, 19, 561, 348, 711, 1):
                游戏结束 = 1

            if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                               pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                rect=[1027, 0, 1124, 45], pattern='PL'):
                return
            if Ocr.mlkitocr_v2(rect=[580, 629, 705, 683], pattern='回'):
                游戏结束 = 1

                click(634, 654)
                time.sleep(6)
            if zi('回', 0, 569, 620, 719, 697, 1):
                游戏结束 = 1

            if Ocr.mlkitocr_v2(rect=[983, 614, 1206, 683], pattern='跳过'):
                游戏结束 = 1
                click(1121, 643)
                time.sleep(2)

            if zi("返回港口", 0, 67, 615, 303, 685, 1) or Ocr.mlkitocr_v2(
                    rect=[67, 615, 303, 685],
                    pattern='升级舰艇'):
                游戏结束 = 1

                time.sleep(0.5)

                click(180, 649)
                time.sleep(4)
            if 游戏结束 == 1:
                if zi('获得', 0, 940, 583, 1237, 717, 1):
                    time.sleep(5)
                    zi('购买', 0, 59, 345, 654, 717)
                    time.sleep(5)
                    zi('购买', 0, 724, 433, 991, 555)
                    time.sleep(3)
                    zi('取消', 0, 308, 453, 580, 547)
                    time.sleep(3)
                    退出()
                    time.sleep(5)
                    if zi("稍后", 0, 662, 592, 937, 708):
                        time.sleep(5)
                        退出()
            if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                               pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                rect=[1027, 0, 1124, 45], pattern='PL'):
                return


    def play():
        global 左右判断, 重启过, 游戏结束, sssj
        sssj = 1
        游戏结束 = 0
        log("开始游戏")
        time.sleep(5)
        if 服务器():
            加入战斗(1)
            time.sleep(2)
            time.sleep(20)
        uiu = 1
        apox = 1
        游戏结束 = 0

        while uiu == 1:
            if stop_event.is_set():
                sssj += 1
                return
            if 闪退() or 重启过 == 1:
                sssj += 1
                return

                # 判断是否进入游戏,寻找蓝色
            if FindColors.find("899,627,#2790A4"):
                uiu += 1
            else:
                time.sleep(5)
                if FindColors.find("899,627,#2790A4"):
                    uiu += 1
                else:
                    # 点击取消的确定,然后继续点击加入战斗
                    tu("确定1", 0, 1, 1, 249, 187, 1121, 623, 1)
                    time.sleep(2)
                    加入战斗(1)
                    time.sleep(2)
                    加入战斗(1)

        战斗 = 1
        pao = 0
        bbbj = 0
        # 前进
        click(196, 498)
        time.sleep(2)
        click(196, 498)
        # Ocr.mlkitocr_v2(rect =[67,615,303,685],pattern = '返回港口')结算
        # Ocr.mlkitocr_v2(rect =[580,629,705,683],pattern = '返回港口') 游戏中
        移动 = 0

        thread1 = threading.Thread(target=结束游戏)
        thread1.start()
        thread2 = threading.Thread(target=跳过)
        thread2.start()
        游戏结束 = 0

        while 战斗 == 1:
            if 游戏结束 == 1:
                sssj += 1
                break

            if 闪退():
                sssj += 1
                重启过 = 1
                return
            if stop_event.is_set():
                sssj += 1
                return
            if 闪退() or 重启过 == 1:
                sssj += 1
                return

                # if FindColors.find("580,316,#F76D67", rect=[92, 229, 1168, 508]) and not Ocr.mlkitocr_v2(rect=[580, 629, 705, 683], pattern='返回港口'):
            #     try:
            #         if 返回港口(1):
            #             return
            #         else:
            #
            #             if FindColors.find("580,316,#F76D67", rect=[767, 119, 1271, 581]):
            #                 if random.random() < 0.3:
            #                     click(303, 541, 2500)
            #                 #右转
            #             else:
            #                 if FindColors.find("580,316,#F76D67", rect=[2, 124, 506, 569]):
            #                     if random.random() < 0.3:
            #                         click(132, 541, 2500)
            #                         # 左转
            #
            #
            #
            #
            #     except AttributeError:
            #         pass

            if 游戏结束 == 0:
                if 游戏结束 == 1:
                    break
                if 寻找目标(10, 173, 1267, 477):
                    if 游戏结束 == 1:
                        break
                else:
                    if not FindColors.find_all("452,345,#FF6D66", rect=[8, 235, 1265, 598]) and 游戏结束 == 0:
                        瞄准(235, 325, 0)
                        time.sleep(1)
                        瞄准(235, 325, 0)
                        if 游戏结束 == 1:
                            break
                        time.sleep(2)
                        if FindColors.find_all("452,345,#FF6D66", rect=[8, 235, 1265, 598]) and 游戏结束 == 0:
                            click(132, 541, 2500)
                            移动 = 10
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            瞄准(1035, 325, 0)
                            time.sleep(1)
                            瞄准(1035, 325, 0)
                            if 游戏结束 == 1:
                                break
                            time.sleep(2)
                            瞄准(1035, 325, 0)
                            time.sleep(1)
                            瞄准(1035, 325, 0)
                            time.sleep(3)

                            if FindColors.find_all("452,345,#FF6D66", rect=[8, 235, 1265, 598]) and 游戏结束 == 0:
                                click(303, 541, 2500)
                                移动 = 10
                                time.sleep(1)
                            else:
                                瞄准(235, 325, 0)
                                time.sleep(1)
                                瞄准(235, 325, 0)

                                time.sleep(3)

                        # if pao == 1:
            #     if not tu("返回港口1", 1, 1, 1, 32, 582, 371, 713, 1):
            #         time.sleep(2)
            #         if tu("加入战斗", 1, 1, 1, 957, 598, 1237, 697, 1):
            #             break

            if 移动 == 0:
                if random.random() < 0.5:
                    click(118, 544, 2000)
                else:
                    if random.random() < 0.5:
                        click(291, 547, 2000)
                if 游戏结束 == 1:
                    break
            else:
                移动 -= 1

            if FindColors.find_all("589,456,#DD1111", rect=[526, 437, 657, 465]) or FindColors.find_all(
                    "575,455,#DD1111", rect=[526, 437, 657, 465]) and 游戏结束 == 0:
                click(212, 590)
                time.sleep(0.2)
                if 游戏结束 == 1:
                    break
                click(215, 602)
                time.sleep(0.2)
                click(215, 602)
                bbbj = 10
            else:
                if 游戏结束 == 1:
                    break

                if bbbj == 0:
                    click(209, 485)
                    time.sleep(0.2)
                    click(209, 485)
                    time.sleep(0.2)
                    click(209, 485)
                else:
                    bbbj -= 1
                    if random.random() < 0.5:
                        click(118, 544, 2000)
                    else:
                        if random.random() < 0.5:
                            click(291, 547, 2000)

            if 寻找目标(10, 173, 1267, 477) and 游戏结束 == 0:
                time.sleep(3)
                if 游戏结束 == 1:
                    break
                if 寻找目标(387, 252, 1033, 522) and 游戏结束 == 0:
                    time.sleep(3)
                    if 游戏结束 == 1:
                        break
                    if 寻找目标(350, 157, 942, 538) and 游戏结束 == 0:
                        time.sleep(2)
                        if 游戏结束 == 1:
                            break
                        if 寻找目标(350, 157, 942, 538) and 游戏结束 == 0:
                            time.sleep(3)
                            if 游戏结束 == 1:
                                break
                        else:
                            continue
                    else:
                        continue

        log("退出战斗")
        thread1.join()
        thread2.join()

if "设定时间":
    time.sleep(2)
    now = datetime.now()
    hourold = now.hour
    minuteold = now.minute
    dayold = now.day
    daynow1 = now.day
    daynow2 = dayold
    hournow1 = now.hour
    hournow2=now.hour
    原始启动时间 = f"{dayold} 日 {hourold} : {minuteold}"

if "邮箱控制":
    def stop_action(x=60):
        global 邮箱控制, wait_time,射击,现次数
        邮箱控制 = 1
        射击=1
        现次数 = 0
        log("收到停止邮件，执行记录暂停时间()")
        记录暂停时间(x)
        wait_time = int(x)
        if wait_time < 1:
            wait_time = 1

        log("等待继续执行")
        stop_event.set()  # 设置停止事件，通知主线程停止
        continue_event.clear()  # 清除继续事件
        # 创建一个线程来运行 wait_and_continue
        继续 = threading.Thread(target=wait_and_continue)

        # 启动线程
        继续.start()

        log("等待继续执行")


    def wait_and_continue():
        log("等待继续执行")
        log(f"等待{wait_time}分钟后将继续执行...")

        time.sleep(wait_time * 60)  # 等待指定时间

        # 检查是否收到“继续”指令
        if 邮箱控制 == 1:
            continue_action()
            # 没有停止事件，继续操作
        else:
            log("等待期间收到了继续邮件，已执行continue_action()，无需继续等待")


    def continue_action():
        global 邮箱控制, 邮箱控制2
        if 邮箱控制 == 1:
            邮箱控制2 = 1
            log("收到继续邮件，执行计算并更新时间() 和重启()")
            计算并更新时间()
            重启()
            stop_event.clear()  # 清除停止事件状态
            continue_event.set()  # 设置继续事件，重新启动任务
            邮箱控制 = 0
            邮箱控制2 = 0
        else:
            email_song(f'{用户邮箱}{设备号},错误操作', '未暂停便继续', f'{报告邮箱}', 4)
            email_song('错误操作', '错误操作\n请先暂停再继续.', f'{用户邮箱}', 4)

if "邮箱":

    class EmailThrottle:
        def __init__(self, interval_minutes=30):
            self.interval = timedelta(minutes=interval_minutes)
            self.last_sent_time = None

        def should_send_email(self):
            now = datetime.now()
            if self.last_sent_time is None or now - self.last_sent_time >= self.interval:
                self.last_sent_time = now
                return True
            return False


    email_throttle = EmailThrottle(间隔时间)


    class EmailThrottle1:
        def __init__(self, interval_minutes=30):
            self.interval = timedelta(minutes=interval_minutes)
            self.last_sent_time = None

        def should_send_email(self):
            now = datetime.now()
            if self.last_sent_time is None or now - self.last_sent_time >= self.interval:
                self.last_sent_time = now
                return True
            return False


    email_throttle1 = EmailThrottle1(用户间隔时间)


    # 需要发送邮件的地方
    def conditionally_send_email(邮件编号, 内容, 用户邮箱):
        # 实例化一个 EmailThrottle 对象
        # 30分钟间隔
        if email_throttle.should_send_email():
            email_song(f'{邮件编号}', f'{内容}', f' {用户邮箱}')
            return True
        else:
            log("跳过邮件发送，因为尚未到达30分钟的间隔")
            return False


    def conditionally_send_email1(邮件编号, 内容, 用户邮箱):
        # 实例化一个 EmailThrottle 对象
        # 30分钟间隔
        if email_throttle1.should_send_email():
            email_song(f'{邮件编号}', f'{内容}', f' {用户邮箱}')
            return True
        else:
            log("跳过邮件发送，因为尚未到达30分钟的间隔")
            return False


    # 示例调用
    def 邮箱():
        global chi, jinbici, chishuyou1, ajinbi5, ajinbi7, chishuyou, ajinbi15, piaoci, apiao10, apiao20, apiao100, yinbici, ayingbi3000, ayingbi1500, ayingbi1000, pjinbi5, pjinbi7, pjinbi15, EXjinbi5, EXjinbi7, EXjinbi15, pjinbi5, pjinbi7, pjinbi15, 期望jinbi5, 期望jinbi7, 期望jinbi15, ppiao10, ppiao20, ppiao100, EXpiao10, EXpiao20, EXpiao100, ppiao10, ppiao20, ppiao100, 期望piao10, 期望piao20, 期望piao100, pyingbi1000, pyingbi1500, pyingbi3000, EXyingbi1000, EXyingbi1500, EXyingbi3000, 期望yingbi1000, 期望yingbi1500, 期望yingbi3000, jinbicha, jinbiold, jinbi, tian, chi, piao, yinbi, xiuli, yanwu, miaohuo, qita, a1aa, 邮件编号, 管理邮件编号, 时长
        if True:

            nowtime(hourold, minuteold, dayold)
            if "防止除零错误":

                if jinbici != 0:
                    ajinbi5 = jinbi5 / jinbici
                    ajinbi7 = jinbi7 / jinbici
                    ajinbi15 = jinbi15 / jinbici
                    ajinbi5 = "{:.2%}".format(ajinbi5)
                    ajinbi7 = "{:.2%}".format(ajinbi7)
                    ajinbi15 = "{:.2%}".format(ajinbi15)
                else:
                    ajinbi5 = "{:.2%}".format(0)
                    ajinbi7 = "{:.2%}".format(0)
                    ajinbi15 = "{:.2%}".format(0)

                if piaoci != 0:
                    apiao10 = piao10 / piaoci
                    apiao20 = piao20 / piaoci
                    apiao100 = piao100 / piaoci
                    apiao10 = "{:.2%}".format(apiao10)
                    apiao20 = "{:.2%}".format(apiao20)
                    apiao100 = "{:.2%}".format(apiao100)
                else:
                    apiao10 = "{:.2%}".format(0)
                    apiao20 = "{:.2%}".format(0)
                    apiao100 = "{:.2%}".format(0)

                if yinbici != 0:
                    ayingbi3000 = yingbi3000 / yinbici
                    ayingbi1500 = yingbi1500 / yinbici
                    ayingbi1000 = yingbi1000 / yinbici
                    ayingbi3000 = "{:.2%}".format(ayingbi3000)
                    ayingbi1500 = "{:.2%}".format(ayingbi1500)
                    ayingbi1000 = "{:.2%}".format(ayingbi1000)
                else:
                    ayingbi3000 = "{:.2%}".format(0)
                    ayingbi1500 = "{:.2%}".format(0)
                    ayingbi1000 = "{:.2%}".format(0)
            if "格式化数据":
                if "细致计算":
                    pjinbi5 = jinbi5 / chi
                    pjinbi7 = jinbi7 / chi
                    pjinbi15 = jinbi15 / chi
                    EXjinbi5 = 5 * pjinbi5
                    EXjinbi7 = 7 * pjinbi7
                    EXjinbi15 = 15 * pjinbi15
                    pjinbi5 = "{:.2%}".format(pjinbi5)

                    pjinbi7 = "{:.2%}".format(pjinbi7)

                    pjinbi15 = "{:.2%}".format(pjinbi15)

                    期望jinbi5 = "{:.3f}".format(EXjinbi5)
                    期望jinbi7 = "{:.3f}".format(EXjinbi7)
                    期望jinbi15 = "{:.3f}".format(EXjinbi15)
                    ppiao10 = piao10 / chi

                    ppiao20 = piao20 / chi

                    ppiao100 = piao100 / chi
                    EXpiao10 = 5 * ppiao10
                    EXpiao20 = 7 * ppiao20
                    EXpiao100 = 15 * ppiao100
                    ppiao10 = "{:.2%}".format(ppiao10)

                    ppiao20 = "{:.2%}".format(ppiao20)

                    ppiao100 = "{:.2%}".format(ppiao100)

                    期望piao10 = "{:.3f}".format(EXpiao10)
                    期望piao20 = "{:.3f}".format(EXpiao20)
                    期望piao100 = "{:.3f}".format(EXpiao100)
                    pyingbi1000 = yingbi1000 / chi

                    pyingbi1500 = yingbi1500 / chi

                    pyingbi3000 = yingbi3000 / chi

                    EXyingbi1000 = 5 * pyingbi1000
                    EXyingbi1500 = 7 * pyingbi1500
                    EXyingbi3000 = 15 * pyingbi3000
                    pyingbi1000 = "{:.2%}".format(pyingbi1000)

                    pyingbi1500 = "{:.2%}".format(pyingbi1500)

                    pyingbi3000 = "{:.2%}".format(pyingbi3000)

                    期望yingbi1000 = "{:.3f}".format(EXyingbi1000)
                    期望yingbi1500 = "{:.3f}".format(EXyingbi1500)
                    期望yingbi3000 = "{:.3f}".format(EXyingbi3000)

                    prob_jinbici = jinbici / chi
                    prob_miaohuoci = miaohuoci / chi
                    prob_yinbici = yinbici / chi
                    prob_xiulici = xiulici / chi
                    prob_piaoci = piaoci / chi
                    prob_yanwuci = yanwuci / chi
                    prob_qitaci = qitaci / chi
                    time.sleep(0.25)
                    formatted_prob_jinbici = "{:.2%}".format(prob_jinbici)
                    formatted_prob_miaohuoci = "{:.2%}".format(prob_miaohuoci)
                    formatted_prob_yinbici = "{:.2%}".format(prob_yinbici)
                    formatted_prob_xiulici = "{:.2%}".format(prob_xiulici)
                    formatted_prob_piaoci = "{:.2%}".format(prob_piaoci)
                    formatted_prob_yanwuci = "{:.2%}".format(prob_yanwuci)
                    formatted_prob_qitaci = "{:.2%}".format(prob_qitaci)
                    time.sleep(0.25)
                    prob_jinbici = jinbici / chi
                    prob_piaoci = piaoci / chi
                    prob_yinbici = yinbici / chi

                    expected_jinbi = 5 * (jinbi5 / chi) + 7 * (jinbi7 / chi) + 15 * (jinbi15 / chi)
                    expected_piao = 10 * (piao10 / chi) + 20 * (piao20 / chi) + 100 * (piao100 / chi)
                    expected_yinbi = 1000 * (yingbi1000 / chi) + 1500 * (yingbi1500 / chi) + 3000 * (
                            yingbi3000 / chi)

                    期望jinbi = "{:.3f}".format(expected_jinbi)
                    期望piao = "{:.3f}".format(expected_piao)
                    期望yinbi = "{:.3f}".format(expected_yinbi)
                    time.sleep(0.25)

                    chi = int(chi)
                    jinbicha = jinbiold - jinbi
                    jinbiold = jinbi

                    jinbi = int(jinbi)
                    piao = int(piao)
                    yinbi = float(yinbi)
                    xiuli = int(xiuli)
                    yanwu = int(yanwu)
                    miaohuo = int(miaohuo)
                    qita = int(qita)

                    # 计算其他相关值
                    tian = "{:.2f}".format(whole_seconds / 86400)

                    xiaoshi = "{:.2f}".format(whole_seconds / 3600)

                    fengzhong = "{:.2f}".format(whole_seconds / 60)
                    aaaas = "{:.2f}".format(whole_seconds / chi)
                    aaaas = float(aaaas)
                    tianchi = "{:.2f}".format(86400 / aaaas)
                    xiaoshici = "{:.2f}".format(float(tianchi) / 24)
                    addds = "{:.2f}".format(aaaas / 60)

                    asads = "{:.2f}".format(aaaas % 60)


                    tian = float(tian)

                    xiaoshi = float(xiaoshi)
                    fengzhong = float(fengzhong)
                    addds = float(addds)

                if "概率统计":
                    金币概率百分比 = 预计几率计算(1500, tianchi, formatted_prob_jinbici, ajinbi5, ajinbi7, ajinbi15,
                                                  5, 7, 15)
                    金币概率百分比1 = 预计几率计算(800, tianchi, formatted_prob_jinbici, ajinbi5, ajinbi7, ajinbi15,
                                                   5, 7, 15)
                    time.sleep(0.25)
                    金币概率百分比2 = 预计几率计算(400, tianchi, formatted_prob_jinbici, ajinbi5, ajinbi7, ajinbi15,
                                                   5, 7, 15)
                    季票概率 = 预计几率计算(1000, tianchi, formatted_prob_piaoci, apiao10, apiao20, apiao100, 10,
                                            20, 100)
                    季票概率1 = 预计几率计算(800, tianchi, formatted_prob_piaoci, apiao10, apiao20, apiao100, 10,
                                             20, 100)
                    time.sleep(0.25)
                    季票概率2 = 预计几率计算(400, tianchi, formatted_prob_piaoci, apiao10, apiao20, apiao100, 10,
                                             20, 100)

                    nowtime(hourold, minuteold, dayold)  # 获取当前时间差
                    转分钟 = 0
                    时长0 = 时长
                    时长小时 = int(时长小时0) + 时长0 * 24 - hours - 总消耗时长小时
                    转分钟 += (时长小时 % 1) * 60
                    时长分钟 = int(时长分钟0) - minutes - 总消耗时长分钟 + 转分钟
                    if 时长分钟 < 0:
                        if 时长小时 > 0:
                            时长小时 -= 1
                            时长分钟 += 60
                        else:
                            a1aa += xunhuanshu
                            重置时间()
                            email_song(f'时长已经用完{用户邮箱} {设备号}',
                                       "时长已经用完", f'{报告邮箱}', 5)
                            email_song(f'时长已经用完',
                                       "时长已经用完", f'{用户邮箱}', 5)
                            return
                    if 时长分钟 < 0:
                        if 时长小时 > 0:
                            时长小时 -= 1
                            时长分钟 += 60
                        else:
                            a1aa += xunhuanshu
                            重置时间()
                            email_song(f'时长已经用完{用户邮箱} {设备号}',
                                       "时长已经用完", f'{报告邮箱}', 5)
                            email_song(f'时长已经用完',
                                       "时长已经用完", f'{用户邮箱}', 5)
                            return
                    时长小时 += 时长分钟 // 60
                    时长0 = 时长小时 // 24
                    时长小时 = 时长小时 % 24
                    save_duration(时长0, 时长小时, 时长分钟)
                    log(时长0, 时长小时, 时长分钟)
                    if 时长 < 0:
                        a1aa += xunhuanshu
                        重置时间()
                        email_song(f'时长已经用完{用户邮箱} {设备号}',
                                   "时长已经用完", f'{报告邮箱}', 5)
                        email_song(f'时长已经用完',
                                   "时长已经用完", f'{用户邮箱}', 5)
                        return
                    bug几率时间=hours*60+minutes+bug时间
                    bug小时 = "{:.2%}".format(bug时间 / bug几率时间)
            if chishuyou >= 用户间隔时间:

                chishuyou = 0
                email_song(f'汇报{邮件编号}',
                           f'开始运行时间    {dayold} 日 {hourold} : {minuteold}\n现在时间    {day}日 {hour} : {minute} : {second}\n已经运行   {hours}  : {minutes} : {secs : .0f} \n剩余时长{时长0}天, {时长小时}小时,{"{:.2f}".format(时长分钟)}分钟, 暂停消耗时长{总消耗时长小时} 小时, {"{:.2f}".format(总消耗时长分钟)}分钟\n原始启动时间{原始启动时间} 崩溃次数 {崩溃次数} Bug次数 {bug数}次 Bug时间 {bug时间}分钟 Bug率 {bug小时}\n服务器问题 {服务器_bug} ,去宝箱界面 {去宝箱界面_bug},赛季任务 {赛季任务_bug} , 进入游戏(海) {进入游戏海_bug} (空) {进入游戏空_bug} ,战斗 (海ai){海战ai_bug} (海) {海战_bug} (空) {战斗空_bug} 更新 {更新shu}\n抽奖次数  {chi},战斗{ju}场 (空) {空战} (海) {海战} , 平均{math.floor(addds)}分钟{asads}秒/次, 预计:\n一天 {tianchi} 次,一小时 {xiaoshici} 次 \n收益:\n获得: 金币 {jinbi} ，季票 {piao} ，银币 {yinbi} ，修理包 {xiuli} 个，烟雾 {yanwu} 个，灭火器 {miaohuo} 个, 海战修理包 {qita} 个，未识别{无法识别}\n次数:金币 {jinbici} 次 ，季票 {piaoci} 次  ，银币 {yinbici} 次 ，修理包 {xiulici} 次，烟雾 {yanwuci} 次，灭火器 {miaohuoci} 次, 海战修理包 {qitaci} 次\n5金币 {jinbi5} 次,7金币 {jinbi7} 次,15金币 {jinbi15} 次,季票,10张 {piao10} 次,20张 {piao20} 次,100张 {piao100} 次,银币1K个 {yingbi1000} 次,1.5K {yingbi1500} 次,3K {yingbi3000} 次\n概率学统计:\n一天1500金币几率{金币概率百分比} ,800金币{金币概率百分比1} ,400金币 {金币概率百分比2} ; 一天1000季票几率{季票概率}, 800季票{季票概率1} ,400季票 {季票概率2}\n期望值:\n金币:{期望jinbi},季票:{期望piao},银币{期望yinbi}\n金币:5个 {期望jinbi5} ,7个 {期望jinbi7} ,15个 {期望jinbi15} \n季票:10张 {期望piao10} ,20张 {期望piao20} ,100张 {期望piao100} \n银币:1K {期望yingbi1000} ,1.5K {期望yingbi1500}  ,3K {期望yingbi3000} \n概率:金币 {formatted_prob_jinbici} ，季票 {formatted_prob_piaoci} ，银币 {formatted_prob_yinbici} ，修理包 {formatted_prob_xiulici} ，烟雾 {formatted_prob_yanwuci} ，灭火器 {formatted_prob_miaohuoci} , 海战修理包 {formatted_prob_qitaci}\n总概率:\n金币:5 ，{pjinbi5} , 7， {pjinbi7} , 15 ，{pjinbi15} ;季票: 10 ，{ppiao10} , 20 ，{ppiao20}, 100  ， {ppiao100} ;银币:1k ，{pyingbi1000} , 1.5k ，{pyingbi1500} , 3k ，{pyingbi3000}\n分概率:\n金币: 5 ，{ajinbi5} , 7 ，{ajinbi7} , 15 ，{ajinbi15}，; 季票:10 ，{apiao10} , 20 ，{apiao20} , 100 ，{apiao100} ; 银币 :1k ，{ayingbi1000} , 1.5k ，{ayingbi1500} , 3k ，{ayingbi3000} \n每次收益为 :  {"{:.2f}".format(jinbi / chi)} 金币, {"{:.2f}".format(piao / chi)} 季票, {"{:.2f}".format(yinbi / chi)} 银币, {"{:.2f}".format(xiuli / chi)} 个修理包, {"{:.2f}".format(yanwu / chi)} 个烟雾, {"{:.2f}".format(miaohuo / chi)} 个灭火器, {"{:.2f}".format(qita / chi)} 个海战修理包\n\n预计收益:\n天收益为 :  {"{:.2f}".format(jinbi / tian)} 金币, {"{:.2f}".format(piao / tian)} 季票, {"{:.2f}".format(yinbi / tian)} 银币, {"{:.2f}".format(xiuli / tian)} 个修理包, {"{:.2f}".format(yanwu / tian)} 个烟雾, {"{:.2f}".format(miaohuo / tian)} 个灭火器, {"{:.2f}".format(qita / tian)} 个海战修理包\n小时收益为 :  {"{:.2f}".format(jinbi / xiaoshi)} 金币, {"{:.2f}".format(piao / xiaoshi)} 季票, {"{:.2f}".format(yinbi / xiaoshi)} 银币, {"{:.2f}".format(xiuli / xiaoshi)} 个修理包, {"{:.2f}".format(yanwu / xiaoshi)} 个烟雾, {"{:.2f}".format(miaohuo / xiaoshi)} 个灭火器, {"{:.2f}".format(qita / xiaoshi)} 个海战修理包\n每分钟收益为 :  {"{:.2f}".format(jinbi / fengzhong)} 金币, {"{:.2f}".format(piao / fengzhong)} 季票, {"{:.2f}".format(yinbi / fengzhong)} 银币, {"{:.2f}".format(xiuli / fengzhong)} 个修理包, {"{:.2f}".format(yanwu / fengzhong)} 个烟雾, {"{:.2f}".format(miaohuo / fengzhong)}  个灭火器, {"{:.2f}".format(qita / fengzhong)} 个海战修理包',
                           f'{用户邮箱}',6)
                邮件编号 += 1
            else:
                chishuyou += 1
            if chishuyou1 >= 间隔时间:

                chishuyou1 = 0
                email_song(f'汇报{管理邮件编号} {用户邮箱}  {设备号}',
                           f'开始运行时间    {dayold} 日 {hourold} : {minuteold}\n现在时间    {day}日 {hour} : {minute} : {second}\n已经运行   {hours}  : {minutes} : {secs : .0f} \n剩余时长{时长0}天, {时长小时}小时,{"{:.2f}".format(时长分钟)}分钟, 暂停消耗时长{总消耗时长小时} 小时, {"{:.2f}".format(总消耗时长分钟)}分钟 \n原始启动时间{原始启动时间} 崩溃次数 {崩溃次数} Bug次数 {bug数}次 Bug时间 {bug时间}分钟 Bug率 {bug小时}\n服务器问题 {服务器_bug} ,去宝箱界面 {去宝箱界面_bug},赛季任务 {赛季任务_bug} , 进入游戏(海) {进入游戏海_bug} (空) {进入游戏空_bug} ,战斗 (海ai){海战ai_bug} (海) {海战_bug} (空) {战斗空_bug} 更新 {更新shu}\n抽奖次数  {chi},战斗{ju}场 (空) {空战} (海) {海战} , 平均{math.floor(addds)}分钟{asads}秒/次, 预计:\n一天 {tianchi} 次,一小时 {xiaoshici} 次 \n收益:\n获得: 金币 {jinbi} ，季票 {piao} ，银币 {yinbi} ，修理包 {xiuli} 个，烟雾 {yanwu} 个，灭火器 {miaohuo} 个, 海战修理包 {qita} 个，未识别{无法识别}\n次数:金币 {jinbici} 次 ，季票 {piaoci} 次  ，银币 {yinbici} 次 ，修理包 {xiulici} 次，烟雾 {yanwuci} 次，灭火器 {miaohuoci} 次, 海战修理包 {qitaci} 次\n5金币 {jinbi5} 次,7金币 {jinbi7} 次,15金币 {jinbi15} 次,季票,10张 {piao10} 次,20张 {piao20} 次,100张 {piao100} 次,银币1K个 {yingbi1000} 次,1.5K {yingbi1500} 次,3K {yingbi3000} 次\n概率学统计:\n一天1500金币几率{金币概率百分比} ,800金币{金币概率百分比1} ,400金币 {金币概率百分比2} ; 一天1000季票几率{季票概率}, 800季票{季票概率1} ,400季票 {季票概率2}\n期望值:\n金币:{期望jinbi},季票:{期望piao},银币{期望yinbi}\n金币:5个 {期望jinbi5} ,7个 {期望jinbi7} ,15个 {期望jinbi15} \n季票:10张 {期望piao10} ,20张 {期望piao20} ,100张 {期望piao100} \n银币:1K {期望yingbi1000} ,1.5K {期望yingbi1500}  ,3K {期望yingbi3000} \n概率:金币 {formatted_prob_jinbici} ，季票 {formatted_prob_piaoci} ，银币 {formatted_prob_yinbici} ，修理包 {formatted_prob_xiulici} ，烟雾 {formatted_prob_yanwuci} ，灭火器 {formatted_prob_miaohuoci} , 海战修理包 {formatted_prob_qitaci}\n总概率:\n金币:5 ，{pjinbi5} , 7， {pjinbi7} , 15 ，{pjinbi15} ;季票: 10 ，{ppiao10} , 20 ，{ppiao20}, 100  ， {ppiao100} ;银币:1k ，{pyingbi1000} , 1.5k ，{pyingbi1500} , 3k ，{pyingbi3000}\n分概率:\n金币: 5 ，{ajinbi5} , 7 ，{ajinbi7} , 15 ，{ajinbi15}，; 季票:10 ，{apiao10} , 20 ，{apiao20} , 100 ，{apiao100} ; 银币 :1k ，{ayingbi1000} , 1.5k ，{ayingbi1500} , 3k ，{ayingbi3000} \n每次收益为 :  {"{:.2f}".format(jinbi / chi)} 金币, {"{:.2f}".format(piao / chi)} 季票, {"{:.2f}".format(yinbi / chi)} 银币, {"{:.2f}".format(xiuli / chi)} 个修理包, {"{:.2f}".format(yanwu / chi)} 个烟雾, {"{:.2f}".format(miaohuo / chi)} 个灭火器, {"{:.2f}".format(qita / chi)} 个海战修理包\n\n预计收益:\n天收益为 :  {"{:.2f}".format(jinbi / tian)} 金币, {"{:.2f}".format(piao / tian)} 季票, {"{:.2f}".format(yinbi / tian)} 银币, {"{:.2f}".format(xiuli / tian)} 个修理包, {"{:.2f}".format(yanwu / tian)} 个烟雾, {"{:.2f}".format(miaohuo / tian)} 个灭火器, {"{:.2f}".format(qita / tian)} 个海战修理包\n小时收益为 :  {"{:.2f}".format(jinbi / xiaoshi)} 金币, {"{:.2f}".format(piao / xiaoshi)} 季票, {"{:.2f}".format(yinbi / xiaoshi)} 银币, {"{:.2f}".format(xiuli / xiaoshi)} 个修理包, {"{:.2f}".format(yanwu / xiaoshi)} 个烟雾, {"{:.2f}".format(miaohuo / xiaoshi)} 个灭火器, {"{:.2f}".format(qita / xiaoshi)} 个海战修理包\n每分钟收益为 :  {"{:.2f}".format(jinbi / fengzhong)} 金币, {"{:.2f}".format(piao / fengzhong)} 季票, {"{:.2f}".format(yinbi / fengzhong)} 银币, {"{:.2f}".format(xiuli / fengzhong)} 个修理包, {"{:.2f}".format(yanwu / fengzhong)} 个烟雾, {"{:.2f}".format(miaohuo / fengzhong)}  个灭火器, {"{:.2f}".format(qita / fengzhong)} 个海战修理包',
                           f'{报告邮箱}',6)
                管理邮件编号 += 1
            else:
                chishuyou1 += 1

            log("正常结束")

if "判断线程":
    def 打开加速器():
        Intent.run("com.github.kr328.clash")
        time.sleep(2)
        Selector().desc("延迟测试").click().find()
        time.sleep(1)
        if not Selector().type("View").packageName("com.github.kr328.clash").maxTextLength(-1).depth(6).find():
            Selector().desc("关闭").click().find()
        time.sleep(1)
        time.sleep(3)
        if Selector().childCount(2).drawingOrder(8).click().find():
            time.sleep(4)
        else:
            if Selector().packageName("com.github.kr328.clash").drawingOrder(7).depth(4).maxTextLength(
                    -1).click().find():
                time.sleep(4)
            if Selector().childCount(2).drawingOrder(8).click().find():
                time.sleep(4)
        Selector().desc("延迟测试").click().find()
        time.sleep(5)
        Selector().drawingOrder(1).depth(6).packageName("com.github.kr328.clash").click().find()
        time.sleep(3)

        Intent.run("com.gaijingames.wtm")
    def 切换加速器():
        global 加速器节点
        if 加速器 == 1:
            action.Key.recents()
            time.sleep(5)
            if tu('biubiu加速器', 0, 1, 1, 277, 82, 1008, 714):
                time.sleep(5)
                Selector().text("停止加速").click().find()
                time.sleep(2)
                Selector().text("停止加速").click().find()
                time.sleep(2)  # 点击退出
                Selector().id("com.njh.biubiu:id/toolbar_left_slot_1").click().find()
                time.sleep(2)
                Selector().id("com.njh.biubiu:id/tv_text").click().find()
                time.sleep(5)
            Intent.run("com.gaijingames.wtm")
        elif 加速器 == 2:
            Intent.run("com.github.kr328.clash")
            time.sleep(2)
            Selector().desc("延迟测试").click().find()
            time.sleep(1)
            if not Selector().type("View").packageName("com.github.kr328.clash").maxTextLength(-1).depth(6).find():
                Selector().desc("关闭").click().find()
                time.sleep(3)
                if Selector().childCount(2).drawingOrder(8).click().find():
                    time.sleep(4)
                else:
                    if Selector().packageName("com.github.kr328.clash").drawingOrder(7).depth(4).maxTextLength(
                            -1).click().find():
                        time.sleep(4)
                    if Selector().childCount(2).drawingOrder(8).click().find():
                        time.sleep(4)

            Selector().desc("延迟测试").click().find()
            time.sleep(5)
            if 加速器节点 == 6:
                加速器节点 -= 5
            Selector().text("🔰 选择节点").click().find()
            Selector().depth(6).drawingOrder(加速器节点).click().find()
            加速器节点 += 1
            time.sleep(3)
            Intent.run("com.gaijingames.wtm")


    # url = "https://1-180-24-8.pd1.cjjd19.com:30443/download-cdn.cjjd19.com/123-355/b2d5aab7/1815582127-0/b2d5aab714bdce45804aeb531e688d63/c-m52?v=5&t=1726598281&s=172659828188ce019e940ebb2fe6cf8a8a3d23c0e1&r=2CNKUX&bzc=1&bzs=1815582127&filename=%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.yaml.txt&x-mf-biz-cid=c94bab66-8697-4b88-97c0-d911d4b76184-6eaa77&auto_redirect=0&cache_type=1&xmfcid=e420c240-3e59-490d-a9f7-9fabd14038bb-0-9eed82220"
    # save_path = "/storage/emulated/0/Download/配置微模块.txt"
    # max_retries = 5  # 最大重试次数
    # retry_delay = 5  # 重试间隔时间（秒）
    # chunk_size = 1024  # 每次读取的字节数
    # progress_interval = 5  # 进度反馈间隔（秒）
    #
    # retries = 0
    # while retries < max_retries:
    #     response = None
    #     try:
    #         response = requests.get(url, stream=True, timeout=60)  # 增加超时时间
    #         if response.status_code == 200:
    #             total_size = int(response.headers.get('content-length', 0))
    #             downloaded_size = 0
    #             last_progress_time = time.time()
    #             with open(save_path, 'wb') as out_file:
    #                 for data in response.iter_content(chunk_size=chunk_size):
    #                     if data:
    #                         out_file.write(data)
    #                         downloaded_size += len(data)
    #                         current_time = time.time()
    #                         if current_time - last_progress_time >= progress_interval:
    #                             log(f"下载进度: {downloaded_size / total_size * 100:.2f}%")
    #                             last_progress_time = current_time
    #             log(f"APK文件已成功下载并保存到: {save_path}")
    #             break  # 下载成功，退出循环
    #         else:
    #             log(f"下载失败，HTTP状态码: {response.status_code}")
    #             break  # 下载失败，退出循环
    #     except requests.exceptions.RequestException as e:
    #         log(f"下载过程中发生错误: {e}")
    #         retries += 1
    #         if retries < max_retries:
    #             log(f"重试下载，第 {retries} 次，等待 {retry_delay} 秒...")
    #             time.sleep(retry_delay)
    #         else:
    #             log("已达到最大重试次数，下载失败。")
    #     finally:
    #         if response is not None:
    #             response.close()
    def 崩溃进程():
        global 崩溃次数, 游戏崩溃, 现次数
        if FindImages.find_all_template([R.img("网络错误.png"), ], rect=[195, 129, 1126, 618],
                                        confidence=0.85) or Selector().text("EXIT").packageName(
            "com.gaijingames.wtm").find():
            log("游戏崩溃")
            现次数 = 0
            崩溃次数 += 1
            游戏崩溃 = 1
            加时间(3)
            stop_event.set()  # 设置停止事件，通知主线程停止
            continue_event.clear()
            time.sleep(60)  # 清除继续事件
            启动()
            stop_event.clear()  # 清除停止事件状态
            continue_event.set()  # 设置继续事件，重新启动任务
            if 是否接受bug信息控制 == 0:
                email_song(f'{用户邮箱},{设备号}游戏崩溃',
                           f'"游戏崩溃',
                           f'{报告邮箱}', 5)
            if 是否接受bug信息用户 == 0:
                email_song('游戏崩溃',
                           f'游戏崩溃',
                           f'{用户邮箱}', 5)


    def main_process():
        global 强行登录, 游戏结束, 崩溃次数, 游戏崩溃, 现次数,是否强行登录
        aaadf = 0
        while True:
            if FindImages.find_all_template([R.img("网络错误.png"), ], rect=[195, 129, 1126, 618],
                                            confidence=0.85) or Selector().text("EXIT").packageName(
                "com.gaijingames.wtm").find():
                log("游戏崩溃")
                现次数 = 0
                崩溃次数 += 1
                游戏崩溃 = 1
                加时间(3)
                stop_event.set()  # 设置停止事件，通知主线程停止
                continue_event.clear()
                time.sleep(60)  # 清除继续事件
                启动()
                stop_event.clear()  # 清除停止事件状态
                continue_event.set()  # 设置继续事件，重新启动任务
                if 是否接受bug信息控制 == 0:
                    email_song(f'{用户邮箱},{设备号}游戏崩溃',
                               f'"游戏崩溃',
                               f'{报告邮箱}', 5)
                if 是否接受bug信息用户 == 0:
                    email_song('游戏崩溃',
                               f'游戏崩溃',
                               f'{用户邮箱}', 5)
            if 正在匹配游戏 == 0 and Ocr.mlkitocr_v2(rect=[311, 144, 1061, 564], pattern='连接丟失'):
                click(645, 496)
            if 邮箱控制 != 1:
                time.sleep(10)
                result = 抢登()
                if result:
                    强行登录 = 1
                    现次数 = 0
                    是否强行登录=1
                    # email_song(f'{用户邮箱},{设备号}抢登成功',
                    #            f'抢登成功,即将暂停,一个小时后会自动继续',
                    #            f'{报告邮箱}', 4)
                    # email_song('抢登成功',
                    #            f'抢登成功,即将暂停,一个小时后会自动继续',
                    #            f'{用户邮箱}', 4)
                    if 邮箱控制 != 1:
                        stop_action()
                        log("等待")
                        time.sleep(60)
                        while 邮箱控制 == 1:
                            time.sleep(60)
                        time.sleep(60)

                    #
                    # # 等待1小时
                    #
                    #     # threading.Thread(target=反抢登).start()
                    #     反抢登()
                    #     强行登录 = 0
                    # 跳出循环，停止检查

            time.sleep(10)  # 每10秒检查一次

    # def 检查崩溃():
    #     global 崩溃次数, 游戏崩溃
    #     while 邮箱控制2 == 1 or 邮箱控制 == 0:
    #
    #
    #
    #         time.sleep(30)

if "战斗动作":
    def 撞墙():
        移动 = 1
        随机移动 = 0
        time.sleep(15)
        yidogg=10
        前进()
        while 游戏结束 == 0:
            # if 随机移动 == 0:
            #     前进()
            if FindColors.find("623,452,#DD1111|617,449,#DD1111",
                               rect=[484, 399, 747, 490]) and 移动 >= 5 and 游戏结束 == 0 or FindColors.find("643,451,#DD1111",rect=[526,434,759,470]) and 移动 >= 6 and 游戏结束 == 0 or FindColors.find("567,453,#DA1313",rect=[516,434,763,483])and 移动 >= 6 and 游戏结束 == 0:

                if random.random() < 0.5:
                    右转(7000)
                else:
                    左转(7000)
                time.sleep(5)
                if FindColors.find("623,452,#DD1111|617,449,#DD1111",
                                   rect=[484, 399, 747, 490]) and 移动 >= 5 and 游戏结束 == 0 or FindColors.find(
                    "643,451,#DD1111", rect=[526, 434, 759, 470]) and 移动 >= 6 and 游戏结束 == 0 or FindColors.find(
                    "567,453,#DA1313", rect=[516, 434, 763, 483]) and 移动 >= 6 and 游戏结束 == 0:

                    后退()
                    后退()
                    后退()
                    time.sleep(15)
                    移动 = 0
                    随机移动 = 1

                    if random.random() < 0.5:
                        右转(7000)
                    else:
                        左转(7000)
                    time.sleep(10)

            else:
                移动 += 1
                time.sleep(1)
                if 移动 == 10:
                    随机移动 = 0
                    移动=0
                if 随机移动 == 1:
                    移动 += 1
            #
            # if FindColors.find("623,452,#DD1111|617,449,#DD1111",
            #                    rect=[484, 399, 747, 490]) and 游戏结束 == 0 and 随机移动 == 0 or FindColors.find("643,451,#DD1111",rect=[526,434,759,470])and 游戏结束 == 0 and 随机移动 == 0:
            #     # 瞄准(435, 325, 0)
            #     # time.sleep(3)
            #     # if 模型("障碍", 0, 586, 187, 693, 515):
            #     #     瞄准(835, 325, 0)
            #     #     if 模型("障碍", 0, 586, 187, 693, 515):
            #     #         if random.random() < 0.5:
            #     #             右转(7000)
            #     #         else:
            #     #             左转(7000)
            #     #     else:
            #     #         右转(5000)
            #     # else:
            #     #     左转(5000)
            #     后退()
            #     time.sleep(15)
            #     if random.random() < 0.5:
            #         右转(7000)
            #     else:
            #         左转(7000)
            #     移动 = 0
            #     随机移动 = 1

            if yidogg>=20 and not FindColors.find("623,452,#DD1111|617,449,#DD1111",
                               rect=[484, 399, 747, 490]) and not FindColors.find("567,453,#DA1313",rect=[516,434,763,483]) and 游戏结束 == 0:
                前进()
                yidogg=0
                if 随机移动 == 0:
                    前进()

            time.sleep(1)
            yidogg+=1


    def 开镜(开1关0=1, 放大大小=0.5):
        # log("判断是否开镜")
        point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
        if point:
            瞄准(point.x, point.y + 30)
            time.sleep(0.5)
        if FindColors.find("746,518,#241F23|751,521,#DDDDDF|755,521,#FFFFFF|757,521,#FFFFFF|742,521,#D2D2D4",
                           rect=[724, 428, 787, 575]):
            # log("开镜状态")
            状态 = 1
        else:
            # log("关镜状态")
            状态 = 0
        if 开1关0 == 1 and 状态 == 1:
            time.sleep(0.3)
            if 放大大小 == 0.5:
                click(744, 506)
            elif 放大大小 == 1:
                click(746, 439)
            elif 放大大小 == 0:
                click(746, 572)
            if FindColors.find("662,190,#FF6D66",rect=[131,21,1203,599],diff=0.96):
                瞄准(881,335)
        elif 开1关0 == 1 and 状态 == 0:
            click(928, 501)
            time.sleep(0.3)
            if 放大大小 == 0.5:
                #click(744, 506)
                click(748,481)
            elif 放大大小 == 1:
                click(746, 439)
            elif 放大大小 == 0:
                #click(746, 572)
                click(748,532)
        elif 开1关0 == 0 and 状态 == 1:
            click(928, 501)
            time.sleep(0.3)
        else:
            if 开1关0 == 0 and 状态 == 0:
                return



    def 前进():
        if FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
                                        confidence=0.90) or FindColors.find("984,407,#53BCCA",
                                                                            rect=[631, 357, 1189, 674]) or Ocr.mlkitocr_v2(rect =[516,541,950,717],pattern = '10'):
            click(209, 498)
            click(209, 498)
            time.sleep(0.5)
            click(209, 498)
            time.sleep(0.5)
            click(209, 498)


    def 后退():
        if FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
                                        confidence=0.90) or FindColors.find("984,407,#53BCCA",
                                                                            rect=[631, 357, 1189, 674]) or Ocr.mlkitocr_v2(rect =[516,541,950,717],pattern = '10'):
            click(206, 598)
            time.sleep(0.5)
            click(206, 598)
            time.sleep(0.5)
            click(206, 598)
            time.sleep(0.5)
            click(206, 598)


    def 左转(x=20):
        if FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
                                        confidence=0.90) or FindColors.find("984,407,#53BCCA",
                                                                            rect=[631, 357, 1189, 674]) or Ocr.mlkitocr_v2(rect =[516,541,950,717],pattern = '10'):
            click(124, 541, x)


    def 右转(x=20):
        if FindImages.find_all_template([R.img("船烟雾.png"), ], rect=[804, 535, 1161, 717],
                                        confidence=0.90) or FindColors.find("984,407,#53BCCA",
                                                                            rect=[631, 357, 1189, 674]) or Ocr.mlkitocr_v2(rect =[516,541,950,717],pattern = '10'):
            click(303, 549, x)

if "海战":
    def play3():
        简单循环 = 0
        global 左右判断, 重启过, 游戏结束, sssj,kekai
        sssj = 1
        kekai=0
        游戏结束 = 0
        log("开始游戏")
        time.sleep(5)
        # 开始进游戏()
        # if 服务器():
        #     加入战斗(1)
        #     time.sleep(2)
        #     time.sleep(20)
        uiu = 1
        apox = 1
        游戏结束 = 0
        qianjin = 0
        # while uiu == 1:
        #     if stop_event.is_set():
        #         sssj += 1
        #         return
        #     if 闪退() or 重启过 == 1:
        #         sssj += 1
        #         return
        #
        #         # 判断是否进入游戏,寻找蓝色
        #     if FindColors.find("899,627,#2790A4"):
        #         uiu += 1
        #     else:
        #         time.sleep(5)
        #         if FindColors.find("899,627,#2790A4"):
        #             uiu += 1
        #         else:
        #             # 点击取消的确定,然后继续点击加入战斗
        #             tu("确定1", 0, 1, 1, 249, 187, 1121, 623, 1)
        #             time.sleep(2)
        #             加入战斗(1)
        #             time.sleep(2)
        #             加入战斗(1)

        战斗 = 1
        pao = 0
        bbbj = 0
        xuanzao = 0
        # 前进

        # Ocr.mlkitocr_v2(rect =[67,615,303,685],pattern = '返回港口')结算
        # Ocr.mlkitocr_v2(rect =[580,629,705,683],pattern = '返回港口') 游戏中
        移动 = 0
        time.sleep(10)
        thread18 = threading.Thread(target=结束游戏)
        thread18.start()
        thread29 = threading.Thread(target=跳过)
        thread29.start()
        thread28 = threading.Thread(target=撞墙)
        thread28.start()
        kaipao = threading.Thread(target=开炮线程)
        kaipao.start()
        游戏结束 = 0
        前进()
        前进()
        if 模型("障碍", 0, 535, 368, 738, 511):
            瞄准(435, 325, 0)
            time.sleep(3)
            if 模型("障碍", 0, 586, 187, 693, 515):
                瞄准(835, 325, 0)
                if 模型("障碍", 0, 586, 187, 693, 515):
                    if random.random() < 0.5:
                        右转(7000)
                    else:
                        if random.random() < 0.5:
                            左转(7000)
                else:
                    右转(5000)
            else:
                左转(5000)
        前进()
        while True:
            if 游戏结束 == 1:
                sssj += 1
                break
            if 闪退():
                sssj += 1
                重启过 = 1
                return
            if stop_event.is_set():
                sssj += 1
                return
            point = FindColors.find("651,265,#FF6D66", rect=[236, 90, 1049, 519])
            if point:
                if point.x > 636:
                    if random.random() < 0.3:
                        右转(2000)
                else:
                    if random.random() < 0.3:
                        左转(2000)
            if 闪退() or 重启过 == 1:
                sssj += 1
                return
            # if qianjin == 10:
            #     click(209, 498)
            #     click(209, 498)
            #     time.sleep(0.5)
            #     click(209, 498)
            #     time.sleep(0.5)
            #     click(209, 498)
            # else:
            #     qianjin += 1
            if 游戏结束 == 1:
                log("等待游戏结束")
                break
            else:
                time.sleep(0.5)
                kekai=1
                if 模型("在目标附近", 1) and FindColors.find("651,265,#FF6D66", rect=[724, 428, 787, 575]) and 模型("敌船", 1):

                    point = FindColors.find("651,265,#FF6D66", rect=[367,60,904,548])
                    if not point:
                        开镜(0)
                        point = FindColors.find("651,265,#FF6D66", rect=[236, 90, 1049, 519])
                        if point:
                            point.y += 30
                            瞄准(point.x, point.y + 60)
                        time.sleep(1)
                        point = FindColors.find("651,265,#FF6D66", rect=[367, 60, 904, 548])
                        if not point:
                            point = FindColors.find("651,265,#FF6D66", rect=[236, 90, 1049, 519])
                            if point:
                                point.y += 30
                                瞄准(point.x, point.y + 60)
                            time.sleep(1)
                    time.sleep(1)
                    if 模型("敌船", 0):
                        瞄准(识别x, 识别y + 10)
                        time.sleep(1.5)
                        # 开炮()
                        time.sleep(1.5)
                        开镜(1, 1)
                        if 模型("敌船", 0):
                            瞄准(识别x, 识别y + 10)
                            # 开炮()

                else:
                        if 模型("在目标附近", 1) and FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500]):
                            point = FindColors.find("651,265,#FF6D66", rect=[236, 90, 1049, 519])
                            if point:
                                if point.x > 636:
                                    if random.random() < 0.3:
                                        右转(2000)
                                else:
                                    if random.random() < 0.3:
                                        左转(2000)
                                point.y += 30
                                瞄准(point.x, point.y + 60)
                            开镜(1, 0.5)
                            point = FindColors.find("651,265,#FF6D66", rect=[236, 90, 1049, 519])
                            if point:
                                瞄准(point.x, point.y + 100)
                            time.sleep(1)
                            if 模型("敌船", 0):
                                瞄准(识别x, 识别y + 10)
                                time.sleep(1.5)
                                # 开炮()
                                time.sleep(1.5)
                                开镜(1, 1)
                                if 模型("敌船", 0):
                                    瞄准(识别x, 识别y + 10)
                                    # 开炮()
                        else:

                            if not 模型("在目标附近", 1):
                                开镜(0)
                                time.sleep(0.5)
                            point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                            if point:
                                if point.x > 636:
                                    if random.random() < 0.3:
                                        右转(2000)
                                else:
                                    if random.random() < 0.3:
                                        左转(2000)
                                point.y += 30
                                瞄准(point.x, point.y, 30)
                                time.sleep(3)
                                开镜(1, 0)
                                if 模型("敌船", 0):
                                    瞄准(识别x, 识别y + 10)
                                    time.sleep(1.5)
                                    # 开炮()
                                    time.sleep(1.5)
                                    开镜(1, 1)
                                    if 模型("敌船", 0, 268, 175, 1017, 530):
                                        瞄准(识别x, 识别y + 5)
                                        # 开炮()
                                kekai = 1
                                point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                                if point:
                                    瞄准(point.x, point.y, 30)
                                    time.sleep(1.5)
                                if 模型("在目标附近", 1):
                                    time.sleep(1.5)
                                    开镜(1)
                                    point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                                    if point:
                                        瞄准(point.x, point.y + 30)
                                        time.sleep(1.5)
                                if 模型("敌船", 0):
                                    瞄准(识别x, 识别y + 10)
                                    time.sleep(1.5)
                                    # 开炮()
                                    time.sleep(1.5)
                                    开镜(1, 1)
                                    if 模型("敌船", 0):
                                        瞄准(识别x, 识别y + 10)
                                        # 开炮()
                            else:
                                kekai = 1
                                # if 模型("在目标附近", 1) and FindColors.find("651,265,#FF6D66",
                                #                                              rect=[5, 137, 1274, 467]):
                                #     time.sleep(1.5)
                                #     开镜(1)
                                #     point = FindColors.find("651,265,#FF6D66", rect=[5, 137, 1274, 467])
                                #     if point:
                                #         瞄准(point.x, point.y + 30)
                                #         time.sleep(1.5)
                                #     if 模型("敌船", 0):
                                #         瞄准(识别x, 识别y + 5)
                                #         time.sleep(1.5)
                                #         # 开炮()
                                #         time.sleep(1.5)
                                #         开镜(1, 1)
                                #         if 模型("敌船", 0, 268, 175, 1017, 530):
                                #             瞄准(识别x, 识别y + 5)
                                #             # 开炮()

                                # 开镜(0)
                                # time.sleep(2)
                                # if 模型("敌人远", 0, 288, 153, 1019, 581):
                                #     瞄准(识别x, 识别y + 30, 5)
                                #     time.sleep(3)
                                #     if 模型("敌船", 0):
                                #         瞄准(识别x, 识别y + 5)
                                #         time.sleep(3)
                                #         开炮()
                                #         time.sleep(3)
                                #         开镜(1, 1)
                                #         if 模型("敌船", 0, 268, 175, 1017, 530):
                                #             瞄准(识别x, 识别y + 5)
                                #             开炮()
                                # else:
                                if xuanzao >= 5:
                                    开镜(0)
                                    if 模型("地平线", 0, 505, 153, 774, 621):
                                        瞄准(识别x, 识别y)
                                        time.sleep(1)
                                    xuanzao = 0
                                    if FindColors.find("651,265,#FF6D66",
                                                       rect=[16, 54, 1274, 500]) and 游戏结束 == 0:
                                        point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                                        if point:
                                            瞄准(point.x, point.y + 30)
                                        continue
                                    瞄准(35, 335, 0)
                                    time.sleep(1)
                                    瞄准(35, 335, 0)
                                    time.sleep(1)
                                    瞄准(35, 335, 0)
                                    time.sleep(1)
                                    瞄准(35, 335, 0)
                                    time.sleep(1)

                                    if FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500]) and 游戏结束 == 0:
                                        point=FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                                        if point:
                                            瞄准(point.x, point.y + 30)

                                        左转(3000)
                                        continue
                                    else:
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        if FindColors.find("651,265,#FF6D66",
                                                           rect=[16, 54, 1274, 500]) and 游戏结束 == 0:
                                            point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                                            if point:
                                                瞄准(point.x, point.y + 30)
                                            continue
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        瞄准(1235, 335, 0)
                                        time.sleep(1)
                                        if FindColors.find("651,265,#FF6D66",
                                                           rect=[16, 54, 1274, 500]) and 游戏结束 == 0:

                                            point = FindColors.find("651,265,#FF6D66", rect=[16, 54, 1274, 500])
                                            if point:
                                                瞄准(point.x, point.y + 30)
                                            右转(3000)
                                            continue
                                        else:
                                            瞄准(35, 335, 0)
                                            time.sleep(1)
                                            瞄准(35, 335, 0)
                                            time.sleep(1)
                                            瞄准(35, 335, 0)
                                            time.sleep(1)
                                            瞄准(35, 335, 0)
                                            time.sleep(1)
                                else:
                                    xuanzao += 1
                                    time.sleep(5)

        log("运行完成")
        kaipao.join()
        thread28.join()
        thread29.join()
        thread18.join()
    def play1():
        简单循环 = 0
        global 左右判断, 重启过, 游戏结束, sssj
        sssj = 1
        游戏结束 = 0
        log("开始游戏")
        time.sleep(5)
        # 开始进游戏()
        # if 服务器():
        #     加入战斗(1)
        #     time.sleep(2)
        #     time.sleep(20)
        uiu = 1
        apox = 1
        游戏结束 = 0
        qianjin = 0
        while uiu == 1:
            if stop_event.is_set():
                sssj += 1
                return
            if 闪退() or 重启过 == 1:
                sssj += 1
                return

                # 判断是否进入游戏,寻找蓝色
            if FindColors.find("899,627,#2790A4"):
                uiu += 1
            else:
                time.sleep(5)
                if FindColors.find("899,627,#2790A4"):
                    uiu += 1
                else:
                    # 点击取消的确定,然后继续点击加入战斗
                    tu("确定1", 0, 1, 1, 249, 187, 1121, 623, 1)
                    time.sleep(2)
                    加入战斗(1)
                    time.sleep(2)
                    加入战斗(1)

        战斗 = 1
        pao = 0
        bbbj = 0
        xuanzao = 0
        # 前进

        # Ocr.mlkitocr_v2(rect =[67,615,303,685],pattern = '返回港口')结算
        # Ocr.mlkitocr_v2(rect =[580,629,705,683],pattern = '返回港口') 游戏中
        移动 = 0
        time.sleep(10)
        thread18 = threading.Thread(target=结束游戏)
        thread18.start()
        thread29 = threading.Thread(target=跳过)
        thread29.start()
        thread28 = threading.Thread(target=撞墙)
        thread28.start()
        游戏结束 = 0
        前进()

        if 模型("障碍", 0, 586, 187, 693, 515):
            瞄准(435, 325, 0)
            time.sleep(3)
            if 模型("障碍", 0, 586, 187, 693, 515):
                瞄准(835, 325, 0)
                if 模型("障碍", 0, 586, 187, 693, 515):
                    if random.random() < 0.5:
                        右转(7000)
                    else:
                        if random.random() < 0.5:
                            左转(7000)
                else:
                    右转(5000)
            else:
                左转(5000)

        while True:
            if 游戏结束 == 1:
                sssj += 1
                break
            if 闪退():
                sssj += 1
                重启过 = 1
                return
            if stop_event.is_set():
                sssj += 1
                return
            if 闪退() or 重启过 == 1:
                sssj += 1
                return
            if qianjin == 10:
                click(209, 498)
                click(209, 498)
                time.sleep(0.5)
                click(209, 498)
                time.sleep(0.5)
                click(209, 498)
            else:
                qianjin += 1
            if 游戏结束 == 1:
                log("等待游戏结束")
                break
            else:
                time.sleep(0.5)
                if 模型("敌人", 0, 288, 153, 1019, 581):

                    瞄准(识别x, 识别y - 15, 5)
                    开镜(1)
                    time.sleep(1)
                    if 模型("敌船", 0, 288, 153, 1019, 581):
                        瞄准(识别x, 识别y, 5)

                    开炮()
                else:
                    if 模型("敌人远", 0, 288, 153, 1019, 581):
                        瞄准(识别x, 识别y - 30, 5)
                        开镜(1)
                    开镜(0)
                    time.sleep(2)

                    if 模型("敌人", 0) and 游戏结束 == 0:
                        开炮()
                        if random.random() < 0.3:
                            click(303, 541, 1500)
                        else:
                            if random.random() < 0.3:
                                click(132, 541, 1500)
                        瞄准(识别x, 识别y - 10, 0)

                        time.sleep(2)
                        if 模型("敌人", 0):
                            瞄准(识别x, 识别y - 15, 0)
                            time.sleep(2)
                            开镜(1, 0)
                            time.sleep(2)
                            if 模型("敌人", 0):
                                瞄准(识别x, 识别y - 15, 0)
                                time.sleep(2)
                            else:
                                开镜(0)
                                continue

                        time.sleep(1)
                        if 模型("敌船", 0):
                            time.sleep(1)
                            瞄准(识别x, 识别y, 5)
                            time.sleep(1)
                            开炮()
                            if 模型("敌船", 0):
                                time.sleep(1)
                                瞄准(识别x, 识别y, 5)
                                time.sleep(1)
                                开炮()
                        else:
                            开镜(0)
                            continue
                    else:
                        if 模型("敌人远", 0) and 游戏结束 == 0:
                            瞄准(识别x, 识别y - 20, 0)

                            time.sleep(2)
                            if 模型("敌人", 0):
                                瞄准(识别x, 识别y - 15, 0)
                                time.sleep(2)
                                开镜(1, 0)
                                time.sleep(2)
                            if 模型("敌人", 0):
                                瞄准(识别x, 识别y - 15, 0)
                                time.sleep(2)
                            else:
                                开镜(0)
                                time.sleep(1)
                            if 模型("敌船", 0):
                                time.sleep(1)
                                瞄准(识别x, 识别y, 5)
                                time.sleep(1)
                                开炮()
                                if 模型("敌船", 0):
                                    time.sleep(1)
                                    瞄准(识别x, 识别y, 5)
                                    time.sleep(1)
                                    开炮()
                            else:
                                开镜(0)
                        else:
                            if xuanzao >= 10:
                                xuanzao = 0
                                瞄准(235, 325, 0)
                                time.sleep(1)
                                瞄准(235, 325, 0)
                                time.sleep(3)
                                if 模型("敌人", 0) and 游戏结束 == 0:
                                    continue
                                else:
                                    复位()
                                    time.sleep(3)
                                    瞄准(1035, 325, 0)
                                    time.sleep(1)
                                    瞄准(1035, 325, 0)
                                    time.sleep(3)
                                    if 模型("敌人", 0) and 游戏结束 == 0:
                                        continue
                                    else:
                                        复位()
                            else:
                                xuanzao += 1

        thread28.join()
        thread29.join()
        thread18.join()

if "空战":
    def play5():
        global 游戏中, 开火x, 开火y, 射击, 锁定x, 锁定, 锁定y
        游戏中 = 0
        ssssss = 0
        fafa = 0
        if FindColors.find("984,407,#53BCCA",
                           rect=[31, 358, 1235,
                                 709]) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
                                                                                                709]) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("机枪.png"), ],
                                                                                    rect=[31, 235, 1265, 708],
                                                                                    confidence=0.95) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("炸弹.png"), ],
                                                                                    rect=[11, 365, 1274, 717],
                                                                                    confidence=0.95) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL'):
            pass
        else:
            开始进游戏空()
        time.sleep(8)
        空战退出进程 = threading.Thread(target=空战退出)
        空战退出进程.start()
        自杀 = 0
        范围内有人 = 0
        自杀值 = 1
        # 瞄准(634, 612, 0)
        while 游戏中 == 0:
            瞄准(634, 612, 0)
            瞄准(634, 612, 0)
            瞄准(634, 612, 0)
            瞄准(634, 612, 0)
            瞄准(634, 612, 0)

            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
        空战退出进程.join()



    def play4():
        global 游戏中, 开火x, 开火y, 射击, 锁定x, 锁定, 锁定y
        游戏中 = 0
        ssssss = 0
        fafa = 0
        if FindColors.find("984,407,#53BCCA",
                           rect=[31, 358, 1235,
                                 709]) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
                                                                                                709]) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("机枪.png"), ],
                                                                                    rect=[31, 235, 1265, 708],
                                                                                    confidence=0.95) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("炸弹.png"), ],
                                                                                    rect=[11, 365, 1274, 717],
                                                                                    confidence=0.95) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL'):
            pass
        else:
            开始进游戏空()
        time.sleep(8)
        空战退出进程 = threading.Thread(target=空战退出)
        空战退出进程.start()
        空中狗斗进程 = threading.Thread(target=空中狗斗)
        空中狗斗进程.start()
        空中动作 = threading.Thread(target=空中战斗)
        if 射击 != 0:
            空中动作.start()
        自杀 = 0
        范围内有人 = 0
        自杀值 = 1
        # 瞄准(634, 612, 0)
        while 游戏中 == 0:
            if 射击 == 0:
                射击 = 1
                res = FindImages.find_all_template([R.img("机枪.png"), ], rect=[31, 235, 1265, 708], confidence=0.95)
                if res:
                    # 遍历所有 找到的结果
                    for i in res:
                        开火x = i["center_x"]
                        开火y = i["center_y"]

                else:
                    res = FindImages.find_all_template([R.img("机枪.png"), ], rect=[31, 235, 1265, 708],
                                                       confidence=0.95)
                    if res:
                        # 遍历所有 找到的结果
                        for i in res:
                            开火x = i["center_x"]
                            开火y = i["center_y"]
                    else:
                        res = FindImages.find_all_template([R.img("炸弹.png"), ], rect=[11, 365, 1274, 717],
                                                           confidence=0.95)
                        if res:
                            # 遍历所有 找到的结果
                            for i in res:
                                开火x = i["center_x"]
                                开火y = i["center_y"]
                adad = FindImages.find_all_template([R.img("锁定.png"), ], confidence=0.80)
                if adad:
                    # 遍历所有 找到的结果
                    for i in adad:
                        锁定x = i["center_x"]
                        锁定y = i["center_y"]
                else:
                    log("未找到锁定")
                    锁定x = 92
                    锁定y = 494
                空中动作.start()

            自杀 += 1
            time.sleep(1.5)
            if 自杀 >= 65:
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)

            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return

        空中狗斗进程.join()
        空中动作.join()
        空战退出进程.join()


    def 空中战斗():
        global 游戏中, 开火x, 开火y, 射击, 锁定x, 锁定, 锁定y
        游戏中 = 0
        sandid = 0
        ssssss = 0
        fafa = 0
        范围内有人 = 0
        while 游戏中 == 0:
            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
            # log("进一步搜索目标")#找人
            if 范围内有人 == 1 and fafa == 1:

                if FindColors.find("205,356,#FF1F1A", rect=[521, 252, 752, 461]) or FindColors.find("383,488,#F56258",
                                                                                                    rect=[521, 252, 752,
                                                                                                          461]) or FindColors.find(
                        "761,232,#DD615F|760,195,#DE786C", rect=[521, 252, 752, 461], diff=0.80) or FindColors.find(
                        "618,269,#D16771|622,233,#D77A82", rect=[521, 252, 752, 461], diff=0.92):
                    # aaaff = FindImages.find_all_template([R.img("红点.png"), ], rect=[230, 134, 428, 365], confidence=0.90)
                    # if aaaff:
                    #     瞄准(aaaff.x, aaaff.y, 0)
                    #     log("找到红点")
                    time.sleep(2)
                    ssssss += 1
                    if ssssss >= 3:
                        范围内有人 = 0
                    continue
            hong = FindColors.find("761,232,#DD615F|760,195,#DE786C", rect=[101, 54, 1205, 687], diff=0.92)
            if hong:
                范围内有人 = 1
                瞄准(hong.x, hong.y, 0)
                log("找到敌机")
                if not FindColors.find(
                        "138,504,#DADADA|102,499,#FFFFFF|100,496,#FFFFFF|76,526,#CBD4D8|77,523,#FFFFFF|124,523,#FFFFFF",
                        rect=[53, 462, 160, 546]) and FindColors.find("761,232,#DD615F|760,195,#DE786C",
                                                                      rect=[101, 54, 1205, 687], diff=0.92):
                    click(锁定x, 锁定y)
                    log("点击锁定")
                    fafa = 1
            else:
                范围内有人 = 0
                hong = FindColors.find("618,269,#D16771|622,233,#D77A82", rect=[101, 54, 1205, 687], diff=0.92)
                if hong:
                    范围内有人 = 1
                    瞄准(hong.x, hong.y, 0)
                    log("找到敌机1")
                    if not FindColors.find(
                            "138,504,#DADADA|102,499,#FFFFFF|100,496,#FFFFFF|76,526,#CBD4D8|77,523,#FFFFFF|124,523,#FFFFFF",
                            rect=[53, 462, 160, 546]):
                        click(锁定x, 锁定y)
                        log("点击锁定")
                        fafa = 1
                else:
                    # hong = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                    #
                    # if hong:
                    #     范围内有人 = 1
                    #     瞄准(hong.x, hong.y, 0)
                    #     log("找到敌方据点")
                    # else:
                    #     范围内有人 = 0
                    #     # 找地面目标
                    #     hong = FindColors.find("383,488,#F56258", rect=[62, 48, 1221, 699])
                    #     if hong:
                    #         范围内有人 = 1
                    #         瞄准(hong.x, hong.y, 0)
                    #         log("找到敌方地面目标")
                    #         continue
                    #     else:
                            范围内有人 = 0
                            sandid += 1
                            if sandid >= 15:
                                sandid = 0
                                # 左边
                                hong = FindColors.find("740,712,#873C3B", rect=[5, 0, 43, 714])
                                if hong:
                                    log("寻找左边")
                                    瞄准(208, 390, 0)
                                    time.sleep(0.5)
                                    瞄准(208, 390, 0)
                                    time.sleep(1)
                                    hong1 = FindColors.find(
                                        "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                        rect=[62, 48, 1221, 699], diff=0.90)
                                    hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                    if not hong1 and not hong2:
                                        瞄准(208, 390, 0)
                                        time.sleep(0.5)
                                        瞄准(208, 390, 0)
                                    else:
                                        continue
                                    time.sleep(1)
                                    hong1 = FindColors.find(
                                        "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                        rect=[62, 48, 1221, 699], diff=0.90)
                                    hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                    if not hong1 and not hong2:
                                        瞄准(208, 390, 0)
                                        time.sleep(0.5)
                                        瞄准(208, 390, 0)
                                    else:
                                        continue
                                    time.sleep(1)
                                    hong1 = FindColors.find(
                                        "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                        rect=[62, 48, 1221, 699], diff=0.90)
                                    hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                    if not hong1 and not hong2:
                                        瞄准(208, 390, 0)
                                        time.sleep(0.5)
                                        瞄准(208, 390, 0)
                                    else:
                                        continue
                                else:
                                    hong = FindColors.find("9,309,#E45655", rect=[5, 0, 43, 714])
                                    if hong:
                                        log("寻找左边")
                                        瞄准(208, 390, 0)
                                        time.sleep(0.5)
                                        瞄准(208, 390, 0)
                                        time.sleep(1)
                                        hong1 = FindColors.find(
                                            "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                            rect=[62, 48, 1221, 699], diff=0.90)
                                        hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                        if not hong1 and not hong2:
                                            瞄准(208, 390, 0)
                                            time.sleep(0.5)
                                            瞄准(208, 390, 0)
                                        else:
                                            continue
                                        time.sleep(1)
                                        hong1 = FindColors.find(
                                            "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                            rect=[62, 48, 1221, 699], diff=0.90)
                                        hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                        if not hong1 and not hong2:
                                            瞄准(208, 390, 0)
                                            time.sleep(0.5)
                                            瞄准(208, 390, 0)
                                        else:
                                            continue
                                        time.sleep(1)
                                        hong1 = FindColors.find(
                                            "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                            rect=[62, 48, 1221, 699], diff=0.90)
                                        hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                        if not hong1 and not hong2:
                                            瞄准(208, 390, 0)
                                            time.sleep(0.5)
                                            瞄准(208, 390, 0)
                                        else:
                                            continue
                                    else:
                                        # 右边

                                        hong = FindColors.find("740,712,#873C3B", rect=[1236, 19, 1280, 711])
                                        if hong:
                                            log("寻找右边")
                                            瞄准(1082, 381, 0)
                                            time.sleep(0.5)
                                            瞄准(1082, 381, 0)
                                            time.sleep(1)
                                            hong1 = FindColors.find(
                                                "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                rect=[62, 48, 1221, 699], diff=0.90)
                                            hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                            if not hong1 and not hong2:
                                                瞄准(1082, 381, 0)
                                                time.sleep(0.5)
                                                瞄准(1082, 381, 0)
                                            else:
                                                continue
                                            time.sleep(1)
                                            hong1 = FindColors.find(
                                                "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                rect=[62, 48, 1221, 699], diff=0.90)
                                            hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                            if not hong1 and not hong2:
                                                瞄准(1082, 381, 0)
                                                time.sleep(0.5)
                                                瞄准(1082, 381, 0)
                                            else:
                                                continue
                                            time.sleep(1)
                                            hong1 = FindColors.find(
                                                "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                rect=[62, 48, 1221, 699], diff=0.90)
                                            hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                            if not hong1 and not hong2:
                                                瞄准(1082, 381, 0)
                                                time.sleep(0.5)
                                                瞄准(1082, 381, 0)
                                            else:
                                                continue
                                        else:
                                            hong = FindColors.find("9,309,#E45655", rect=[1236, 19, 1280, 711])
                                            if hong:
                                                log("寻找右边")
                                                瞄准(1082, 381, 0)
                                                time.sleep(0.5)
                                                瞄准(1082, 381, 0)
                                                time.sleep(1)
                                                hong1 = FindColors.find(
                                                    "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                    rect=[62, 48, 1221, 699], diff=0.90)
                                                hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                                if not hong1 and not hong2:
                                                    瞄准(1082, 381, 0)
                                                    time.sleep(0.5)
                                                    瞄准(1082, 381, 0)
                                                else:
                                                    continue
                                                time.sleep(1)
                                                hong1 = FindColors.find(
                                                    "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                    rect=[62, 48, 1221, 699], diff=0.90)
                                                hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                                if not hong1 and not hong2:
                                                    瞄准(1082, 381, 0)
                                                    time.sleep(0.5)
                                                    瞄准(1082, 381, 0)
                                                else:
                                                    continue
                                                time.sleep(1)
                                                hong1 = FindColors.find(
                                                    "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                    rect=[62, 48, 1221, 699], diff=0.90)
                                                hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                                if not hong1 and not hong2:
                                                    瞄准(1082, 381, 0)
                                                    time.sleep(0.5)
                                                    瞄准(1082, 381, 0)
                                                else:
                                                    continue
                                            else:
                                                # 下面

                                                hong = FindColors.find("740,712,#873C3B", rect=[27, 703, 1241, 714])
                                                if hong:
                                                    log("寻找下面")
                                                    瞄准(640, 644, 0)
                                                    time.sleep(0.5)
                                                    瞄准(640, 644, 0)

                                                    time.sleep(1)
                                                    hong1 = FindColors.find(
                                                        "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                        rect=[62, 48, 1221, 699], diff=0.90)
                                                    hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                                    if not hong1 and not hong2:
                                                        瞄准(640, 644, 0)
                                                        time.sleep(0.5)
                                                        瞄准(640, 644, 0)
                                                    else:
                                                        continue
                                                    time.sleep(1)
                                                    hong1 = FindColors.find(
                                                        "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                        rect=[62, 48, 1221, 699], diff=0.90)
                                                    hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                                    if not hong1 and not hong2:
                                                        瞄准(640, 644, 0)
                                                        time.sleep(0.5)
                                                        瞄准(640, 644, 0)
                                                    else:
                                                        continue
                                                    time.sleep(1)
                                                    hong1 = FindColors.find(
                                                        "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                        rect=[62, 48, 1221, 699], diff=0.90)
                                                    hong2 = FindColors.find("205,356,#FF1F1A", rect=[62, 48, 1221, 699])
                                                    if not hong1 and not hong2:
                                                        瞄准(640, 644, 0)
                                                        time.sleep(0.5)
                                                        瞄准(640, 644, 0)
                                                    else:
                                                        continue
                                                else:
                                                    hong = FindColors.find("9,309,#E45655", rect=[27, 703, 1241, 714])
                                                    if hong:
                                                        log("寻找下面")
                                                        瞄准(640, 644, 0)
                                                        time.sleep(0.5)
                                                        瞄准(640, 644, 0)
                                                        time.sleep(1)
                                                        hong1 = FindColors.find(
                                                            "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                            rect=[62, 48, 1221, 699], diff=0.90)
                                                        hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                rect=[62, 48, 1221, 699])
                                                        if not hong1 and not hong2:
                                                            瞄准(640, 644, 0)
                                                            time.sleep(0.5)
                                                            瞄准(640, 644, 0)
                                                        else:
                                                            continue
                                                        time.sleep(1)
                                                        hong1 = FindColors.find(
                                                            "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                            rect=[62, 48, 1221, 699], diff=0.90)
                                                        hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                rect=[62, 48, 1221, 699])
                                                        if not hong1 and not hong2:
                                                            瞄准(640, 644, 0)
                                                            time.sleep(0.5)
                                                            瞄准(640, 644, 0)
                                                        else:
                                                            continue
                                                        time.sleep(1)
                                                        hong1 = FindColors.find(
                                                            "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                            rect=[62, 48, 1221, 699], diff=0.90)
                                                        hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                rect=[62, 48, 1221, 699])
                                                        if not hong1 and not hong2:
                                                            瞄准(640, 644, 0)
                                                            time.sleep(0.5)
                                                            瞄准(640, 644, 0)
                                                        else:
                                                            continue
                                                    else:
                                                        # 上面
                                                        hong = FindColors.find("740,712,#873C3B", rect=[5, 2, 1222, 23])
                                                        if hong:
                                                            log("寻找上面")

                                                            瞄准(640, 16, 0)
                                                            time.sleep(0.5)
                                                            瞄准(640, 16, 0)
                                                            time.sleep(1)
                                                            hong1 = FindColors.find(
                                                                "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                                rect=[62, 48, 1221, 699], diff=0.90)
                                                            hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                    rect=[62, 48, 1221, 699])
                                                            if not hong1 and not hong2:
                                                                瞄准(640, 16, 0)
                                                                time.sleep(0.5)
                                                                瞄准(640, 16, 0)
                                                            else:
                                                                continue
                                                            time.sleep(1)
                                                            hong1 = FindColors.find(
                                                                "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                                rect=[62, 48, 1221, 699], diff=0.90)
                                                            hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                    rect=[62, 48, 1221, 699])
                                                            if not hong1 and not hong2:
                                                                瞄准(640, 16, 0)
                                                                time.sleep(0.5)
                                                                瞄准(640, 16, 0)
                                                            else:
                                                                continue
                                                            time.sleep(1)
                                                            hong1 = FindColors.find(
                                                                "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                                rect=[62, 48, 1221, 699], diff=0.90)
                                                            hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                    rect=[62, 48, 1221, 699])
                                                            if not hong1 and not hong2:
                                                                瞄准(640, 16, 0)
                                                                time.sleep(0.5)
                                                                瞄准(640, 16, 0)
                                                            else:
                                                                continue
                                                        else:
                                                            hong = FindColors.find("9,309,#E45655",
                                                                                   rect=[5, 2, 1222, 23])
                                                            if hong:
                                                                log("寻找上面")
                                                                瞄准(640, 16, 0)
                                                                time.sleep(0.5)
                                                                瞄准(640, 16, 0)
                                                                time.sleep(1)
                                                                hong1 = FindColors.find(
                                                                    "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                                    rect=[62, 48, 1221, 699], diff=0.90)
                                                                hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                        rect=[62, 48, 1221, 699])
                                                                if not hong1 and not hong2:
                                                                    瞄准(640, 16, 0)
                                                                    time.sleep(0.5)
                                                                    瞄准(640, 16, 0)
                                                                else:
                                                                    continue
                                                                time.sleep(1)
                                                                hong1 = FindColors.find(
                                                                    "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                                    rect=[62, 48, 1221, 699], diff=0.90)
                                                                hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                        rect=[62, 48, 1221, 699])
                                                                if not hong1 and not hong2:
                                                                    瞄准(640, 16, 0)
                                                                    time.sleep(0.5)
                                                                    瞄准(640, 16, 0)
                                                                else:
                                                                    continue
                                                                time.sleep(1)
                                                                hong1 = FindColors.find(
                                                                    "1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                                                                    rect=[62, 48, 1221, 699], diff=0.90)
                                                                hong2 = FindColors.find("205,356,#FF1F1A",
                                                                                        rect=[62, 48, 1221, 699])
                                                                if not hong1 and not hong2:
                                                                    瞄准(640, 16, 0)
                                                                    time.sleep(0.5)
                                                                    瞄准(640, 16, 0)
                                                                else:
                                                                    continue


    def 移除载具():
        if Ocr.mlkitocr_v2(rect=[266, 615, 453, 684], pattern='空') and Ocr.mlkitocr_v2(rect=[466, 607, 640, 681],
                                                                                        pattern='空') and Ocr.mlkitocr_v2(
            rect=[659, 610, 848, 681], pattern='空'):
            log("没有多余载具")
        else:
            log("发现多余载具")
            退出()
            click(96, 497)
            time.sleep(0.5)
            if not Ocr.mlkitocr_v2(rect=[266, 615, 453, 684], pattern='空'):
                click(351, 634)
                time.sleep(0.5)
                click(991, 645)
                time.sleep(0.5)
            if not Ocr.mlkitocr_v2(rect=[466, 607, 640, 681], pattern='空'):
                click(541, 645)
                time.sleep(0.5)
                click(991, 645)
            if not Ocr.mlkitocr_v2(rect=[659, 610, 848, 681], pattern='空'):
                click(736, 643)
                time.sleep(0.5)
                click(991, 645)
            退出()


    def 空战退出():
        global 游戏中

        while True:
            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
            if 加入战斗():
                游戏中 = 1
                if FindColors.find("72,39,#FFFFFF|73,58,#FFFFFF|70,74,#FFFFFF", rect=[34, 5, 122, 103]):
                    click(82, 57)
                    time.sleep(1)
                    click(442, 491)


            if zi("跳过", 0, 961, 601, 1233, 706, 1):
                time.sleep(1.5)
                游戏中 = 1
            if zi("获取", 0, 939, 574, 1227, 700, 1):
                time.sleep(1.5)
                游戏中 = 1
                if zi("条件", 0, 220, 28, 413, 90):
                    time.sleep(1.5)
                    click(379, 311)
                    time.sleep(0.5)
                    click(291, 314)
                    time.sleep(0.5)
                    click(201, 320)
                    time.sleep(0.5)
                    click(124, 303)
                    time.sleep(2)
                    click(804, 167)
                    time.sleep(1.5)
                    sjdi = FindColors.find("701,278,#E19608", rect=[161, 87, 1144, 620])
                    if sjdi:
                        click(sjdi.x, sjdi.y)
                        time.sleep(4.5)
                        if zi("开始研发", 0, 873, 604, 1142, 700, 1):
                            time.sleep(4.5)
                            time.sleep(1.5)
                            if zi("接受", 0, 703, 423, 977, 541, 1):
                                time.sleep(1.5)
            if zi("跳过", 0, 961, 601, 1233, 706, 1):
                time.sleep(1.5)
                游戏中 = 1
            if FindColors.find_all(
                    "496,467,#C07737|507,471,#A76730|511,462,#A96A32|509,467,#A6662F|504,467,#C77A38|501,470,#905929|500,462,#FE9D47",
                    rect=[411, 78, 593, 514]):
                游戏中 = 1
                try:
                    # log("进一步搜索目标")
                    hong = FindColors.find_all(
                        "496,467,#C07737|507,471,#A76730|511,462,#A96A32|509,467,#A6662F|504,467,#C77A38|501,470,#905929|500,462,#FE9D47",
                        rect=[411, 78, 593, 514])
                    click(hong.x, hong.y)
                    time.sleep(4.5)
                    if zi("开始研发", 0, 873, 604, 1142, 700, 1):
                        time.sleep(4.5)
                        time.sleep(1.5)
                        if zi("接受", 0, 703, 423, 977, 541, 1):
                            time.sleep(1.5)
                except AttributeError:
                    # log("未找到目标")
                    time.sleep(1.5)
            if zi("跳过", 0, 961, 601, 1233, 706, 1):
                time.sleep(1.5)
                游戏中 = 1
            if zi("返回基地", 0, 49, 604, 335, 698, 1) or zi("新乘员组", 0, 48, 586, 325, 699, 1):
                游戏中 = 1

            if 退出():
                游戏中 = 1

            if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90], pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                    rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(rect=[791, 35, 1181, 90],
                                                                               pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                rect=[1027, 0, 1124, 45], pattern='PL'):
                游戏中 = 1
                return
            if zi("跳过", 0, 961, 601, 1233, 706, 1):
                time.sleep(1.5)
                游戏中 = 1




    def 空中狗斗():
        while 游戏中 == 0:
            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
            if FindColors.find("1151,269,#E06D66|1150,268,#DF6E68|1151,270,#E16D6D|1149,271,#D1717C",
                               rect=[576, 302, 708, 417], diff=0.90) or FindColors.find("205,356,#FF1F1A",
                                                                                        rect=[576, 302, 708,
                                                                                              417]) or FindColors.find(
                "383,488,#F56258", rect=[576, 302, 708, 417]):
                click(开火x, 开火y, 1500)
                time.sleep(5)


    射击 = 0
    开火x = 966
    开火y = 447


    def play2():
        global 游戏中, 开火x, 开火y, 射击
        游戏中 = 0
        if FindColors.find("984,407,#53BCCA",
                           rect=[31, 358, 1235,
                                 709]) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindColors.find("997,462,#54BCCA", rect=[31, 358, 1235,
                                                                                                709]) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("机枪.png"), ],
                                                                                    rect=[31, 235, 1265, 708],
                                                                                    confidence=0.95) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL') or FindImages.find_all_template([R.img("炸弹.png"), ],
                                                                                    rect=[11, 365, 1274, 717],
                                                                                    confidence=0.95) and Ocr.mlkitocr_v2(
            rect=[1027, 0, 1124, 45], pattern='PL'):
            pass
        else:
            开始进游戏空()
        time.sleep(8)
        空战退出进程 = threading.Thread(target=空战退出)
        空战退出进程.start()
        空中狗斗进程 = threading.Thread(target=空中狗斗)
        空中狗斗进程.start()
        自杀 = 0
        范围内有人 = 0
        自杀值 = 1
        瞄准(634, 612, 0)
        while 游戏中 == 0:
            if 射击 == 0:
                res = FindImages.find_all_template([R.img("机枪.png"), ], rect=[31, 235, 1265, 708], confidence=0.95)
                if res:
                    # 遍历所有 找到的结果
                    for i in res:
                        开火x = i["center_x"]
                        开火y = i["center_y"]

                else:
                    res = FindImages.find_all_template([R.img("机枪.png"), ], rect=[31, 235, 1265, 708],
                                                       confidence=0.95)
                    if res:
                        # 遍历所有 找到的结果
                        for i in res:
                            开火x = i["center_x"]
                            开火y = i["center_y"]
                    else:
                        res = FindImages.find_all_template([R.img("炸弹.png"), ], rect=[11, 365, 1274, 717],
                                                           confidence=0.95)
                        if res:
                            # 遍历所有 找到的结果
                            for i in res:
                                开火x = i["center_x"]
                                开火y = i["center_y"]

                射击 = 1

            自杀 += 1
            瞄准(634, 612, 0)
            if 自杀 % 4 == 0:  # 10%的几率执行
                if 范围内有人 == 0:
                    自杀值 += 1
                if 范围内有人 == 0 and 自杀值 >= 10 and FindColors.find("9,592,#E7534C", rect=[153, 667, 1117, 711]):
                    自杀值 = 0
                    瞄准(634, 612, 0)
                    time, sleep(1)
                    瞄准(634, 612, 0)
                    瞄准(634, 612, 0)
                    time, sleep(1)
                    瞄准(634, 612, 0)
                    瞄准(634, 612, 0)
                    time, sleep(1)
                    瞄准(634, 612, 0)
                if 范围内有人 == 0 and 自杀值 >= 10 and FindColors.find("9,592,#E7534C", rect=[2, 36, 59, 714]):
                    自杀值 = 0
                    瞄准(237, 442, 0)
                    瞄准(237, 442, 0)
                    瞄准(237, 442, 0)
                    瞄准(237, 442, 0)
                elif 范围内有人 == 0 and 自杀值 >= 10 and FindColors.find("9,592,#E7534C", rect=[1234, 51, 1277, 705]):
                    自杀值 = 0
                    瞄准(900, 493, 0)
                    瞄准(900, 493, 0)
                    瞄准(900, 493, 0)
                    瞄准(900, 493, 0)
                elif   范围内有人 == 0 and 自杀值 >= 10 and random.random() < 0.1:
                    自杀值 = 0
                    瞄准(730, 365, 0)
                elif  范围内有人 == 0 and 自杀值 >= 10 and random.random() < 0.2:
                    自杀值 = 0
                    瞄准(414, 360, 0)
                elif   范围内有人 == 0 and 自杀值 >= 10 and random.random() < 0.3:
                    自杀值 = 0
                    瞄准(634, 612, 0)
            if 自杀 >= 40:
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)
                瞄准(634, 612, 0)

            if stop_event.is_set():
                return
            if 闪退() or 重启过 == 1:
                return
            try:
                # log("进一步搜索目标")
                hong = FindColors.find("598,211,#D8666A", rect=[28,24,1259,683])
                if hong:
                    范围内有人 = 1
                else:
                    范围内有人 = 0
                瞄准(hong.x, hong.y, 0)
            except AttributeError:
                try:
                    hong = FindColors.find("619,354,#EF7672", rect=[28,24,1259,683])
                    if hong:
                        范围内有人 = 1
                    else:
                        范围内有人 = 0
                    瞄准(hong.x, hong.y, 0)
                except AttributeError:
                    try:
                        hong = FindColors.find("461,485,#FF201B", rect=[28,24,1259,683])
                        if hong:
                            范围内有人 = 1
                        else:
                            范围内有人 = 0
                        瞄准(hong.x, hong.y, 0)
                    except AttributeError:
                        # log("未找到目标")
                        time.sleep(1.5)

            time.sleep(2.5)
        空中狗斗进程.join()
        空战退出进程.join()

if 模式==1:
    打开加速器()
    启动()
else:
    启动()
    退出()
if "转换字符串":

    res = Ocr.paddleocr_v2(rect=[141, 31, 546, 79])
    if res:
        # 循环打印识别到的每一个段落
        for r in res:
            玩家名 = r.text
    if 箱子 == 0:
        箱子字 = "不开启"
    elif 箱子 == 1:
        箱子字 = "仅开启陆战"
    elif 箱子 == 2:
        箱子字 = "仅开启海战"
    else:
        箱子字 = "全开启"

    if 战斗模式 == 1:
        战斗模式字 = "识别颜色战斗"
    elif 战斗模式 == 2:
        战斗模式字 = "弱Ai识别战斗"
    elif 战斗模式 == 3:
        战斗模式字 = "空战图色识别"
    if 是否接受bug信息用户 == 1:
        是否接受bug信息用户字 = "不接收bug信息"
    elif 是否接受bug信息用户 == 0:
        是否接受bug信息用户字 = "接收bug信息"
    if 是否接受bug信息控制 == 1:
        是否接受bug信息控制字 = "不接收bug信息"
    elif 是否接受bug信息控制 == 0:
        是否接受bug信息控制字 = "接收bug信息"

Dialog.toast('开始执行')
# 保存时间
read_and_set_values()
yolo = YoLov5("zhanlei:1.1")
if "开始邮件发送" and not DEBUG:
    首次 = 0
    if 是否首次 == 1:
        email_song(f'{用户邮箱},{设备号}升级脚本,及重启脚本,版本 {版本}',
                   f"玩家名字(不准确):{玩家名}   ,注意 海战布局请恢复默认,不要在不玩是选择潜艇 ,海战灵敏度为15% 15% 开启自动放大不开启  ,,,空战右边开火位置需要在默认位置其他随意            \n是否接受bug信息用户字 {是否接受bug信息用户字}\n更新脚本运行状态,返厂宝箱购买设置 {箱子字},单次连续战斗数 {单次游戏局数}局, 战斗选择海战占比 {随机战斗模式} ,战斗模式设置  {战斗模式字},自动继续时间 {自动继续时间}分钟\n剩余时长  {时长}天, {时长小时0}小时,{时长分钟0}分钟\n\n\n1.当要玩时可以用邮件停止运行脚本，暂停时长，\n使用接收邮箱发送x是非负数,可以暂停x小时后自动继续脚本,也可以不加x,默认1小时后自动继续脚本\n主题为:停止x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n!!!也可以直接强行登录,一个小时后会自动继续脚本可设置自定义继续时间\n主题为:自动继续时间x\n的邮件到\nt_yang_only@qq.com  \n其中x为数字默认单位为分钟\n\n2，不玩时，或者还没到自动继续的时间,可以使用\n主题为:继续\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n4,如果需要做赛季任务\n主题为:赛季任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n需要很长时间主要,可以用邮件停止\n主题为:赛季任务关\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n同理把'赛季'替换'活动'可做活动任务\n\n5,可以自动进行日常任务,一天一次\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n如果需要关闭,可以用邮件停止\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开\n6,如果有返厂宝箱,银币箱,可以自动开启x为0到3 ,如上\n主题为:宝箱x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n\n7，!!!!!!!!!如果玩海战，请继续脚本是恢复界面布局,海战选择的船最好是脆皮,推荐1,2级船\n\n8，长时间未反回邮件  界面bug，请联系作者，\n或者进行邮件控制\n主题为:重启\n的邮件到t_yang_only@qq.com\n也可以联系作者\nyysbsbsb@163.com\n##如果嫌邮件太过频繁可以发送  \n主题为:间隔时间x   \n到t_yang_only@qq.com(x为游戏局数)  以下为专业设置 可自己理解 单次游戏局数 = 3随机战斗模式 = 0.2  #为百分比 1 为100%海战战斗模式 = 2  #1 海战图色识别 #2 海战Ai 接受bug信息  不接受bug信息   #极限模式开 极限模式关",
                   f'{报告邮箱}', 5)
        email_song(f'升级脚本,及重启脚本,版本 {版本}',
                   f"玩家名字(不准确):{玩家名} ,注意 海战布局请恢复默认,不要在不玩是选择潜艇 ,海战灵敏度为15% 15% 开启自动放大不开启  ,,,空战右边开火位置需要在默认位置其他随意              \n是否接受bug信息用户字 {是否接受bug信息用户字}\n更新脚本运行状态,返厂宝箱购买设置 {箱子字},单次连续战斗数 {单次游戏局数}局,战斗选择海战占比 {随机战斗模式}  ,战斗模式设置  {战斗模式字},自动继续时间 {自动继续时间}分钟\n {时长}天, {时长小时0}小时,{时长分钟0}分钟\n\n\n1.当要玩时可以用邮件停止运行脚本，暂停时长，\n使用接收邮箱发送x是非负数,可以暂停x小时后自动继续脚本,也可以不加x,默认1小时后自动继续脚本\n主题为:停止x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n!!!也可以直接强行登录,一个小时后会自动继续脚本可设置自定义继续时间\n主题为:自动继续时间x\n的邮件到\nt_yang_only@qq.com  \n其中x为数字默认单位为分钟\n\n2，不玩时，或者还没到自动继续的时间,可以使用\n主题为:继续\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n4,如果需要做赛季任务\n主题为:赛季任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n需要很长时间主要,可以用邮件停止\n主题为:赛季任务关\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n同理把'赛季'替换'活动'可做活动任务\n\n5,可以自动进行日常任务,一天一次\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n如果需要关闭,可以用邮件停止\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开\n6,如果有返厂宝箱,银币箱,可以自动开启x为0到3 ,如上\n主题为:宝箱x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n\n7，!!!!!!!!!如果玩海战，请继续脚本是恢复界面布局,海战选择的船最好是脆皮,推荐1,2级船\n\n8，长时间未反回邮件  界面bug，请联系作者，\n或者进行邮件控制\n主题为:重启\n的邮件到t_yang_only@qq.com\n也可以联系作者\nyysbsbsb@163.com\n##如果嫌邮件太过频繁可以发送  \n主题为:间隔时间x   \n到t_yang_only@qq.com(x为游戏局数)以下为专业设置 可自己理解 单次游戏局数 = 3随机战斗模式 = 0.2  #为百分比 1 为100%海战战斗模式 = 2  #1 海战图色识别 #2 海战Ai 接受bug信息  不接受bug信息 #极限模式开 极限模式关",
                   f'{用户邮箱}', 5)

    else:
        email_song(f'{用户邮箱},{设备号}程序运行,版本 {版本}',
                   f'玩家名字(不准确):{玩家名}   ,注意 海战布局请恢复默认,不要在不玩是选择潜艇 ,海战灵敏度为15% 15% 开启自动放大不开启  ,,,空战右边开火位置需要在默认位置其他随意               \n是否接受bug信息用户字 {是否接受bug信息用户字}\n返厂宝箱购买设置 {箱子字},单次连续战斗数 {单次游戏局数}局,战斗选择海战占比 {随机战斗模式}  ,战斗模式设置  {战斗模式字},自动继续时间 {自动继续时间}分钟\n时长  {时长}天, {时长小时0}小时,{时长分钟0}分钟 开始运行时间 {dayold} 日 {hourold} : {minuteold}\n\n1.当要玩时可以用邮件停止运行脚本，暂停时长，\n使用接收邮箱发送x是非负数,可以暂停x小时后自动继续脚本,也可以不加x,默认1小时后自动继续脚本\n主题为:停止x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n!!!也可以直接强行登录,一个小时后会自动继续脚本可设置自定义继续时间\n主题为:自动继续时间x\n的邮件到\nt_yang_only@qq.com  \n其中x为数字默认单位为分钟\n\n2，不玩时，或者还没到自动继续的时间,可以使用\n主题为:继续\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n4,如果需要做赛季任务\n主题为:赛季任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n需要很长时间主要,可以用邮件停止\n主题为:赛季任务关\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n同理把 赛季 替换 活动 可做活动任务\n\n5,可以自动进行日常任务,一天一次\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n如果需要关闭,可以用邮件停止\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开\n6,如果有返厂宝箱,银币箱,可以自动开启x为0到3 ,如上\n主题为:宝箱x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n\n7，!!!!!!!!!如果玩海战，请继续脚本是恢复界面布局,海战选择的船最好是脆皮,推荐1,2级船\n\n8，长时间未反回邮件  界面bug，请联系作者，\n或者进行邮件控制\n主题为:重启\n的邮件到t_yang_only@qq.com\n也可以联系作者\nyysbsbsb@163.com\n##如果嫌邮件太过频繁可以发送  \n主题为:间隔时间x   \n到t_yang_only@qq.com(x为游戏局数)以下为专业设置 可自己理解 单次游戏局数 = 3随机战斗模式 = 0.2  #为百分比 1 为100%海战战斗模式 = 2  #1 海战图色识别 #2 海战Ai 接受bug信息  不接受bug信息 #极限模式开 极限模式关',
                   f'{报告邮箱}', 5)
        email_song(f'程序运行,及详细操作,版本 {版本}',
                   f'玩家名字(不准确):{玩家名}   ,注意 海战布局请恢复默认,不要在不玩是选择潜艇 ,海战灵敏度为15% 15% 开启自动放大不开启  ,,,空战右边开火位置需要在默认位置其他随意              \n是否接受bug信息用户字 {是否接受bug信息用户字}\n 返厂宝箱购买设置 {箱子字},单次连续战斗数 {单次游戏局数}局,战斗选择海战占比 {随机战斗模式}  ,战斗模式设置  {战斗模式字},自动继续时间 {自动继续时间}分钟\n脚本开始运行\n如果需要游玩直接登录即可,也可以先发出按照指令再开始游戏.\n时长 {时长}天, {时长小时0}小时,{时长分钟0}分钟 开始运行时间 {dayold} 日 {hourold} : {minuteold}\n\n1.当要玩时可以用邮件停止运行脚本，暂停时长，\n使用接收邮箱发送x是非负数,可以暂停x小时后自动继续脚本,也可以不加x,默认1小时后自动继续脚本\n主题为:停止x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n!!!也可以直接强行登录,一个小时后会自动继续脚本,可设置自定义继续时间\n主题为:自动继续时间x\n的邮件到\nt_yang_only@qq.com  \n其中x为数字默认单位为分钟\n\n2，不玩时，或者还没到自动继续的时间,可以使用\n主题为:继续\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n4,如果需要做赛季任务\n主题为:赛季任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n需要很长时间主要,可以用邮件停止\n主题为:赛季任务关\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n同理把 赛季 替换 活动 可做活动任务\n\n5,可以自动进行日常任务,一天一次\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n如果需要关闭,可以用邮件停止\n主题为:日常任务开\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n箱子 = 0  #0不开启  #1开启陆战 #2开启海战 #3全开\n6,如果有返厂宝箱,银币箱,可以自动开启x为0到3 ,如上\n主题为:宝箱x\n的邮件到\nt_yang_only@qq.com\n当成功后会有返回邮件\n\n\n7，!!!!!!!!!如果玩海战，请继续脚本是恢复界面布局,海战选择的船最好是脆皮,推荐1,2级船\n\n8，长时间未反回邮件  界面bug，请联系作者，\n或者进行邮件控制\n主题为:重启\n的邮件到t_yang_only@qq.com\n也可以联系作者\nyysbsbsb@163.com\n##如果嫌邮件太过频繁可以发送  \n主题为:间隔时间x   \n到t_yang_only@qq.com(x为游戏局数)以下为专业设置 可自己理解 单次游戏局数 = 3随机战斗模式 = 0.2  #为百分比 1 为100%海战战斗模式 = 2  #1 海战图色识别 #2 海战Ai  接受bug信息  不接受bug信息 # 极限模式开 极限模式关',
                   f'{用户邮箱}', 5)

def task_function():
    global a1aa, 游戏崩溃, 重启了,海1空2, xunhuanshu, 上次是海1空2, 现次数, ju, 重启过, daynow1, daynow2, chi, 进入游戏空_bug, 进入游戏海_bug, 赛季任务_bug, 去宝箱界面_bug, 服务器_bug, 海战, 海战_bug, 海战ai_bug, 空战, 战斗空_bug, 单次游戏局数
    while True:
        if stop_event.is_set():
            log("任务已停止，等待继续命令...")
            continue_event.wait()  # 等待继续事件被设置
        while a1aa <= xunhuanshu:
            if stop_event.is_set():
                break
            try:
                if "流程":
                    pass
                if "收益进程":
                    if not stop_event.is_set() and 赛季任务 == 1 and 现次数 == 0:
                        if 闪退():
                            break
                        if 执行函数(赛季, 1200):
                            加时间(20)
                            赛季任务_bug += 1
                            if 是否接受bug信息用户 == 0:
                                email_song('界面Bug',
                                           f'"赛季任务"函数卡住20分钟,即将重启软件,初始时间加20分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{用户邮箱}', 5)
                            if 是否接受bug信息控制 == 0:
                                email_song(f'{用户邮箱},{设备号}界面Bug',
                                           f'"赛季任务"函数卡住20分钟,即将重启软件,初始时间加20分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{报告邮箱}', 5)

                            continue
                        time.sleep(1)
                    if not stop_event.is_set() and 赛季任务 == 2 and 现次数 == 0:
                        if 闪退():
                            break
                        if 执行函数(赛季1, 1200):
                            加时间(20)
                            赛季任务_bug += 1
                            if 是否接受bug信息用户 == 0:
                                email_song('界面Bug',
                                           f'"赛季任务"函数卡住20分钟,即将重启软件,初始时间加20分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{用户邮箱}', 5)
                            if 是否接受bug信息控制 == 0:
                                email_song(f'{用户邮箱},{设备号}界面Bug',
                                           f'"赛季任务"函数卡住20分钟,即将重启软件,初始时间加20分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{报告邮箱}', 5)

                            continue
                        time.sleep(1)
                    if 重启过 == 1:
                        重启过 = 0
                        continue

                    # 去宝箱界面
                    if not stop_event.is_set() and 赛季任务 != 1 and 现次数 == 0 and 赛季任务 != 2:
                        if 闪退():
                            break
                        if not stop_event.is_set() and 执行函数(去宝箱界面, 360):
                            加时间(6)
                            去宝箱界面_bug += 1
                            if 是否接受bug信息控制 == 0:
                                email_song(f'{用户邮箱},{设备号}界面Bug',
                                           f'"去宝箱界面"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{报告邮箱}', 5)
                            if 是否接受bug信息用户 == 0:
                                email_song('界面Bug',
                                           f'"去宝箱界面"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{用户邮箱}', 5)

                            continue
                        time.sleep(1)
                    if 重启过 == 1:
                        重启过 = 0
                        continue

                    # 抽奖
                    if not stop_event.is_set() and 赛季任务 != 1 and 现次数 == 0 and 赛季任务 != 2:
                        if 闪退():
                            break
                        if 执行函数(抽奖, 2100):
                            加时间(20)
                            服务器_bug += 1
                            if 是否接受bug信息控制 == 0:
                                email_song(f'{用户邮箱},{设备号}界面Bug',
                                           f'"抽奖"函数卡住35分钟,即将重启软件,初始时间加35分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{报告邮箱}', 5)
                            if 是否接受bug信息用户 == 0:
                                email_song('服务器寄了,界面Bug',
                                           f'服务器寄了,即将重启软件,并切换加速节点,初始时间加35分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                           f'{用户邮箱}', 5)
                            continue
                        time.sleep(1)
                        if 重启过 == 1:
                            重启过 = 0
                            continue

                # if 游戏崩溃 == 0:
                #     首次空 = 0
                # else:
                #     游戏崩溃 = 1
                海1空2 = 0
                if Ocr.mlkitocr_v2(rect=[273, 153, 1010, 575], pattern='tomorrow'):
                    time.sleep(1)
                    click(687, 479)
                    单次游戏局数=20
                退出()
                while 现次数 <= 单次游戏局数 and not stop_event.is_set():
                    if stop_event.is_set():
                        break
                    现次数 += 1
                    # time.sleep(3)
                    if 加入战斗():
                        time.sleep(2)
                    else:
                        zi("取消", 0, 322, 439, 563, 549)
                        time.sleep(2)
                        if Ocr.mlkitocr_v2(rect=[673, 609, 926, 685], pattern='稍后'):
                            time.sleep(4)
                            click(815, 649)
                            time.sleep(3)
                            退出()
                            time.sleep(3)
                        退出()
                    # 开始进游戏

                    if 重启过 == 1:
                        重启过 = 0
                        continue
                    # play
                    if not stop_event.is_set():
                        空战 += 1
                        log("空战模式")
                        if not stop_event.is_set():
                            if 闪退():
                                break
                        if 闪退():
                            break
                        ju += 1
                        if 极限模式==1:
                            if 海1空2 == 2:
                                海1空2 = 2
                            else:
                                切换模式(3)
                                海1空2 = 2
                            if 现次数 == 1 or 重启了 == 0:
                                移除载具()

                            if 执行函数(开始进游戏空, 360):
                                加时间(6)
                                进入游戏空_bug += 1

                                if 是否接受bug信息控制 == 0:
                                    email_song(f'{用户邮箱},{设备号}界面Bug',
                                               f'"开始进游戏空"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                               f'{报告邮箱}', 5)
                                if 是否接受bug信息用户 == 0:
                                    email_song('界面Bug',
                                               f'"开始进游戏空"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                               f'{用户邮箱}', 5)
                                # 切换模式(3)
                                海1空2 = 0

                                # 重启了 = 0
                                continue
                            time.sleep(5)
                            if 执行函数(play5, 500):
                                加时间(8)
                                战斗空_bug += 1
                                if 是否接受bug信息控制 == 0:
                                    email_song(f'{用户邮箱},{设备号}界面Bug',
                                               f'"play2"函数卡住8分钟,即将重启软件,初始时间加8分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                               f'{报告邮箱}', 5)
                                if 是否接受bug信息用户 == 0:
                                    email_song('界面Bug',
                                               f'游戏过程卡住8分钟,即将重启软件,初始时间加8分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                               f'{用户邮箱}', 5)
                                # 切换模式(3)
                                # 重启了=1
                                海1空2 = 0

                                continue
                            continue
                        if random.random() < 随机战斗模式 and 极限模式==0:
                            log("海战模式")
                            海战 += 1
                            # if 现次数 == 1 or 重启了==0:
                            #     重启了=1
                            #     上次是海1空2 = 1

                            # if 上次是海1空2 == 2:
                            #     切换模式(1)
                            #     上次是海1空2 = 1

                            if not stop_event.is_set():
                                if 闪退():
                                    break
                                # while True:
                                #     if stop_event.is_set():
                                #         return
                                #     if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90],
                                #                        pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                                #         rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(
                                #         rect=[791, 35, 1181, 90],
                                #         pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                                #         rect=[1027, 0, 1124, 45], pattern='PL'):
                                #         break
                                #     退出()
                                #     if zi("返回基地", 0, 19, 561, 348, 711, 1) or zi("返回港口", 0, 19, 561, 348, 711,
                                #                                                      1):
                                #         pass
                                #
                                #     if zi("返回港口", 0, 67, 615, 303, 685, 1) or Ocr.mlkitocr_v2(
                                #             rect=[67, 615, 303, 685],
                                #             pattern='升级舰艇'):
                                #         time.sleep(0.5)
                                #
                                #         click(180, 649)
                                #         time.sleep(4)
                                #     if True:
                                #         if zi('获得', 0, 940, 583, 1237, 717, 1):
                                #             time.sleep(5)
                                #             zi('购买', 0, 59, 345, 654, 717)
                                #             time.sleep(5)
                                #             zi('购买', 0, 724, 433, 991, 555)
                                #             time.sleep(3)
                                #             zi('取消', 0, 308, 453, 580, 547)
                                #             time.sleep(3)
                                #             退出()
                                #             time.sleep(5)
                                #             if zi("稍后", 0, 662, 592, 937, 708):
                                #                 time.sleep(5)
                                #
                                退出()
                                if 海1空2==1:
                                    海1空2=1
                                else:
                                    切换模式(1)
                                    海1空2 = 1

                                if 执行函数(开始进游戏, 360):
                                    加时间(6)
                                    进入游戏海_bug += 1

                                    if 是否接受bug信息控制 == 0:
                                        email_song(f'{用户邮箱},{设备号}界面Bug',
                                                   f'"开始进游戏海"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{报告邮箱}', 5)
                                    if 是否接受bug信息用户 == 0:
                                        email_song('界面Bug',
                                                   f'"开始进游戏海"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{用户邮箱}', 5)

                                    # 切换模式(1)
                                    海1空2=0

                                    # 重启了 = 0
                                    continue
                                time.sleep(1)
                            if 战斗模式 == 1:

                                if 执行函数(play, 720):
                                    加时间(12)
                                    海战_bug += 1
                                    if 是否接受bug信息控制 == 0:
                                        email_song(f'{用户邮箱},{设备号}界面Bug',
                                                   f'海战bug12分钟,即将重启软件,初始时间加12分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{报告邮箱}', 5)
                                    if 是否接受bug信息用户 == 0:
                                        email_song('界面Bug',
                                                   f'游戏过程卡住12分钟,即将重启软件,初始时间加12分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{用户邮箱}', 5)
                                    # 切换模式(1)
                                    海1空2=0
                                    continue
                            elif 战斗模式 == 2:
                                if 执行函数(play3, 720):
                                    海战ai_bug += 1
                                    加时间(12)
                                    if 是否接受bug信息控制 == 0:
                                        email_song(f'{用户邮箱},{设备号}界面Bug',
                                                   f'海战bug12分钟,即将重启软件,初始时间加12分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{报告邮箱}', 5)
                                    if 是否接受bug信息用户 == 0:
                                        email_song('界面Bug',
                                                   f'游戏过程卡住12分钟,即将重启软件,初始时间加12分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{用户邮箱}', 5)
                                    # 切换模式(1)
                                    海1空2=0

                                    # 重启了=0
                                    continue



                        else:
                            空战 += 1
                            log("空战模式")
                            if not stop_event.is_set():
                                if 闪退():
                                    break
                                # if 上次是海1空2 == 1:
                                #     切换模式(3)
                                #     上次是海1空2 = 2
                                # while True:
                                #     if stop_event.is_set():
                                #         return
                                #     if Ocr.mlkitocr_v2(rect=[866, 47, 986, 90],
                                #                        pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(
                                #         rect=[1027, 0, 1124, 45], pattern='PL') or Ocr.mlkitocr_v2(
                                #         rect=[791, 35, 1181, 90],
                                #         pattern='\\d+') and 加入战斗() and not Ocr.mlkitocr_v2(rect=[1027, 0, 1124, 45],
                                #                                                                pattern='PL'):
                                #         break
                                #
                                #     if zi("跳过", 0, 961, 601, 1233, 706, 1):
                                #         time.sleep(1.5)
                                #         游戏中 = 1
                                #     if zi("获取", 0, 939, 574, 1227, 700, 1):
                                #         time.sleep(1.5)
                                #         游戏中 = 1
                                #
                                #     if FindColors.find_all(
                                #             "496,467,#C07737|507,471,#A76730|511,462,#A96A32|509,467,#A6662F|504,467,#C77A38|501,470,#905929|500,462,#FE9D47",
                                #             rect=[411, 78, 593, 514]):
                                #         游戏中 = 1
                                #         try:
                                #             # log("进一步搜索目标")
                                #             hong = FindColors.find_all(
                                #                 "496,467,#C07737|507,471,#A76730|511,462,#A96A32|509,467,#A6662F|504,467,#C77A38|501,470,#905929|500,462,#FE9D47",
                                #                 rect=[411, 78, 593, 514])
                                #             click(hong.x, hong.y)
                                #             time.sleep(4.5)
                                #             if zi("开始研发", 0, 873, 604, 1142, 700, 1):
                                #                 time.sleep(4.5)
                                #                 time.sleep(1.5)
                                #                 if zi("接受", 0, 703, 423, 977, 541, 1):
                                #                     time.sleep(1.5)
                                #         except AttributeError:
                                #             # log("未找到目标")
                                #             time.sleep(1.5)
                                #     if zi("返回基地", 0, 49, 604, 335, 698, 1) or zi("新乘员组", 0, 48, 586, 325, 699,
                                #                                                      1):
                                #         游戏中 = 1
                                #
                                #     if 退出():
                                #         游戏中 = 1
                                if 海1空2==2:
                                    海1空2=2
                                else:
                                    切换模式(3)
                                    海1空2 = 2
                                if 现次数 == 1 or 重启了 == 0:
                                    移除载具()

                                if 执行函数(开始进游戏空, 360):
                                    加时间(6)
                                    进入游戏空_bug += 1

                                    if 是否接受bug信息控制 == 0:
                                        email_song(f'{用户邮箱},{设备号}界面Bug',
                                                   f'"开始进游戏空"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{报告邮箱}', 5)
                                    if 是否接受bug信息用户 == 0:
                                        email_song('界面Bug',
                                                   f'"开始进游戏空"函数卡住6分钟,即将重启软件,初始时间加6分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{用户邮箱}', 5)
                                    # 切换模式(3)
                                    海1空2=0

                                    # 重启了 = 0
                                    continue
                                time.sleep(5)
                            if 执行函数(play4, 500):
                                    加时间(8)
                                    战斗空_bug += 1
                                    if 是否接受bug信息控制 == 0:
                                        email_song(f'{用户邮箱},{设备号}界面Bug',
                                                   f'"play2"函数卡住8分钟,即将重启软件,初始时间加8分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{报告邮箱}', 5)
                                    if 是否接受bug信息用户 == 0:
                                        email_song('界面Bug',
                                                   f'游戏过程卡住8分钟,即将重启软件,初始时间加8分钟,开始运行时间变为 {dayold} 日 {hourold} : {minuteold}',
                                                   f'{用户邮箱}', 5)
                                    # 切换模式(3)
                                    # 重启了=1
                                    海1空2 = 0

                                    continue
                else:
                    现次数=1


                if 重启过 == 1:
                        重启过 = 0
                        continue

                # if 上次是海1空2 == 1:
                #     pass
                # else:
                #     切换模式(1)
                #     上次是海1空2 == 1
                # 邮箱

                # 游戏崩溃=0
                if not stop_event.is_set() and 赛季任务 != 1:

                    a1aa += 1
                    if 是否切换载具==1 and 极限模式==0:

                        随机切换载具()
                    elif 是否切换载具==1 and 随机战斗模式==1:
                        切海()
                    elif  是否切换载具==1 and 极限模式==1:
                        切空()
                    try:

                        ju = float(ju)

                        if 检查时间执行广告():
                            单次游戏局数=10
                            现次数 =0
                        if 日常任务 == 1:
                            检查日期变化并执行任务()
                        邮箱线程 = threading.Thread(target=邮箱)
                        邮箱线程.start()

                        # 创建一个线程来执行邮箱函数

                    except Exception as e:
                        email_song(f'{设备号}错误{用户邮箱}', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}', 5)

            except Exception as e:
                email_song(f'{设备号}错误{用户邮箱}', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}', 5)
                错误()

            log("正常结束")

            time.sleep(1)
        log("循环结束，准备开始新的循环...")


while True:
    try:
        # 邮件接收线程
        email_thread13 = threading.Thread(target=connect_email_by_pop3)
        email_thread13.start()
        # 检查强登线程
        task_thread13 = threading.Thread(target=main_process)
        task_thread13.start()

        # 主线程任务
        task_thread21 = threading.Thread(target=task_function)
        task_thread21.start()
        # task_thread55 = threading.Thread(target=检查崩溃)
        # task_thread55.start()

        try:
            email_thread13.join()
            task_thread13.join()
            task_thread21.join()
            # task_thread55.join()
        except Exception as e:
            email_song('主线程中断', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}')
        finally:
            stop_event.set()  # 确保在退出前停止所有线程
            continue_event.set()  # 确保在退出前不再等待
            log("所有线程已停止")
    except Exception as e:
        restarts += 1
        if restarts > 100:  # 如果重启次数超过100次，则发送邮件并退出程序
            email_song('重启次数过多', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}')
            break
        else:
            email_song('重启线程', f'{e}{e.__traceback__.tb_lineno}', f'{报告邮箱}')
            time.sleep(30)  # 等待一段时间再重启
