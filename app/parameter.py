# coding: utf-8

# dynamic create menu
menus = [
        {
            'label': "主页",
            'path': '/pages/index'
            },
        {
            'label': "校友活动",
            'path': '/pages/alumni_activities'
            },
        {
            'label': "全球疫情动态",
            #'path': '/pages/wuhan_situation'
            'path': '/reports'
            },
        {
            'label': "校友会在行动",
            'path': '/pages/alumni_action'
            },
        {
            'label': "捐赠方式和公示",
            'path': '/pages/donate'
            },
        {
            'label': "历史通知和公告",
            'path': '/notices'
            },
        {
            'label': "联系我们",
            'path': '/pages/contact_us'
            },
        {
            'label': "Q&A",
            'path': '/pages/qa'
            },
        ]

# information about index pages
index_info = {
  'home_images': ["image/alumni_activities/2018_bbq.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_activities/2017_bbq.jpg", "image/alumni_activities/2017_admin.jpg", \
                   "image/alumni_activities/2018_prof.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_activities/2007_president.jpg"  ],

    'alumni_association': {
      'title': "武汉大学北加州校友会",
      'content': "武汉大学北加州校友会，草创于1980年代，由部分台湾来美和大陆来美的武大校友联合倡议，于1998年正式成立于加州硅谷，是武汉大学校友总会认可的合法合规海外校友会分支，是基金会的执行机构。",
      'member_info': {
          'cur_title': "校友会会长:",
          'cur_member': ["巨辉 (现任会长)", "陶然 (副会长)", "Harry Wang (副会长)", "沈睿 (副会长)", "李晨晨 (副会长)"],
          'pre_title': "历任校友会会长:",
          'pre_member': ["王常玉（首任会长)", "陈海雷", "张露", "欧阳明", "陈小春", "陈章鸿", "李金辉"]
      },
      'legality': {
          'title': "机构资质认定 - 序号211",
          'link': "https://alumni.whu.edu.cn/gdxyh.htm"
      }
    },

    'foundation': {
      'title': "武汉大学海外校友科学基金会",
      'content': "在武汉大学杰出校友黄彰任先生倡议下，通过王高峰，王常玉，李晓景等武汉大学校友的积极筹划准备，基金会成立于1999年，是美国联邦注册非营利性公益组织、公共慈善机构，符合美国《内部税收法》第501（c）（3）条规定的免税的联邦公益组织。",
      'member_info': {
          'title': "基金会历任会长:",
          'member': ["黄彰任（名誉会长)", "王高峰", "李晓景（首任会长)", "宁挺", "王常玉", "欧阳明", "陈小春", "李金辉 (现任会长)"],
      },
      'hzr': {
        'image': 'image/hzr.jpg',
        'title': '黄彰任，武汉大学北加州校友会名誉会长',
        'source': {
          'title': "",
          'content': "Link",
          'link': 'https://alumni.whu.edu.cn/info/1054/8102.htm',
        },

        'content': '武汉大学土木系校友 （1938届），武汉大学第一届杰出校友, 美国密歇根大学硕士（1952届），美国国会顾问，泰国森美实业公司董事长。 是一位享誉世界的华人实业家，也是一位享誉世界的华人慈善家。曾任任1940s国民革命军空军总部科长，1950—1951年 台湾大学土木系副教授，1953—1954年 任美国密歇根州公路局桥梁工程师；美国J.G.WHITE纽约总公司结构工程师；1955—1981年 任泰国森美实业公司总经理和泰国森美石油公司董事长。先后在美国纽约设立黄彰任基金会,在美国史丹福大学、康州州立大学等处设立奖学金。在瑞士设立欧阳遇基金会,资助赴欧美留学深造的家乡学子。捐资修建长沙雅礼中学彰任图书馆和平江县欧阳遇图书馆。1996年，捐资20万美元，在母校武汉大学设立奖励基金，1996年，捐助10万美元在史丹福大学设立黄彰任奖学基金，1994年，捐助10万美元在史丹福大学医院设立肝脏移植中心，1995年，在黄彰任80寿辰之日，美国旧金山市将这一天定为“黄彰任日”，这是对黄彰任一生杰出成就给予的最崇高的荣誉。2001年，武汉大学设立“黄彰任信息技术研究所”，王高峰教授担任所长，周怀北，胡继承任副所长。2012年10月30日，黄彰任先生在美国洛杉矶因病去世。'
      },
      'wgf': {
        'title': '王高峰',
        'content': "武汉大学空间物理系校友，斯坦福大学科学计算博士、威斯康辛大学密尔沃基分校电子工程（EE）博士，中国国家杰出青年科学基金获得者，英国工程技术学会会士。曾在Synopsys公司和贝尔实验室等机构进行多年的科学研究，并在美国硅谷先后创办了英迪光讯公司（Intpax, Inc.）和矽翔微机电系统有限公司（Siargo Ltd.）。在武汉大学先后创建黄彰任信息技术研究所（2001年）和微电子与信息技术研究院（2004年）。王高峰教授已经发表科研论文450余篇，撰写1本专著和6个书籍章节，共获得48项已授权专利。2005年入选（马奎斯）美国名人录，2006年入选（马奎斯）世界名人录和（马奎斯）科学工程名人录。"
      }
    },
    'special_topic': [
    {
      'title': ["疫情动态","我要捐赠"],
      'image': "image/jiayou.jpeg",
      'link': ['wuhan_situation', 'donate']
    },
    {
      'title': ["联系我们"],
      'image': "image/alumni_activities/2017_alumni.jpg",
      'link': ['contact_us']
    }
    ]

}

# information about index pages
alumni_activities_info = {
  'home_images': ["image/alumni_activities/2018_bbq.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_activities/2017_bbq.jpg", "image/alumni_activities/2017_admin.jpg", \
                   "image/alumni_activities/2018_prof.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_activities/2007_president.jpg"  ],

  'introduction': [
        "武汉大学北加州校友会成立伊始，就本着团结武汉海外校友，凝聚武大海外力量，扩大武大海外影响力，连接武大与美国加州的目的，组织了一系列社交，学术，交流，对接等活动，获得校友的大力支持和武汉大学，武汉大学校友总会的认可和肯定。校友活动包括一年一度的校友新春联欢，年度中秋BBQ聚会，武汉大学代表团接待，武汉大学学生海外游学团接待，并积极参与旧金山总领事管组织的新春团拜，跨校友会合作等活动。在祖国需要海外支援时，包括2003年非典疫情，2008年汶川地震等积极募捐资金和物资支援祖国。",
        "对于此次爆发于武汉的2019-nCoV疫情，校友更是十分牵挂母校和武汉疫情防控，在第一时间校友会开展募捐资金和紧缺医疗物资支援行动，团结广大的北加州校友和北美校友，协调广泛的校友力量，社会力量和美国民间力量，及时协调筹集了大批物资送到一线医护人员手上，更多的校友会支援武汉行动依然在进行。",
        "众志成城，抗击疫情，校友会在行动！武汉加油，中国加油！"
    ],


  'activites_info': [
    {
      'title': "2019年10月 校友会年度BBQ (拔河掠影)",
      'image': ["image/alumni_activities/2019_bbq_1.jpg", "image/alumni_activities/2019_bbq_2.jpg"]
    }, 
    {
      'title': "2019年10月 校友会协办3551国际创业大赛(硅谷赛区)",
      'image': ["image/alumni_activities/2019_3551.jpg"]
    }, 
    {
      'title': "2019年8月校友会对接生命科学院暑期访学团",
      'image': ["image/alumni_activities/2019_life_science_1.jpg", "image/alumni_activities/2019_life_science_2.jpg"]
    }, 
    {
      'title': "2018年12 武大校友同武大院士教授欢聚",
      'image': ["image/alumni_activities/2018_prof.jpg"]
    }, 
    {
      'title': "2018年10月 校友会年度BBQ合影",
      'image': ["image/alumni_activities/2018_bbq.jpg"]
    }, 
    {
      'title': "2018年10月校友会协办3551国际创业大赛(硅谷赛区)",
      'image': ["image/alumni_activities/2018_3551.jpg"]
    }, 
    {
      'title': "2018年8月校友会对接生命科学院暑期访学团",
      'image': ["image/alumni_activities/2018_life_science.jpg"]
    }, 
    {
      'title': "2018年8月校友会代表队参与第16届北加州华人文化体育协会运动大会",
      'image': ["image/alumni_activities/2018_sport_meet_1.jpg", "image/alumni_activities/2018_sport_meet_2.jpg"]
    }, 
    {
      'title': "2018年4月 武大校董喻鹏和新一届校友会成员一起",
      'image': ["image/alumni_activities/2018_university_council.jpg"]
    }, 
    {
      'title': "2017年 窦贤康校长与校友会在斯坦福组织武大海外恳谈会",
      'image': ["image/alumni_activities/2017_president.jpg"]
    }, 
    {
      'title': "2017年武大校友会全体人员",
      'image': ["image/alumni_activities/2017_alumni.jpg"]
    }, 
    {
      'title': "2017年校友会年度BBD(联合兄弟校友会和湖北同乡会)",
      'image': ["image/alumni_activities/2017_bbq.jpg"]
    }, 
    {
      'title': "2015年11月 武汉大学副校长黄泰岩 在湾区招才引智",
      'image': ["image/alumni_activities/2015_vice_president.jpg"]
    }, 
    {
      'title': "2010年 武大校长刘经南到湾区看望武大校友",
      'image': ["image/alumni_activities/2010_president.jpg"]
    }, 
    {
      'title': "2007年12月 黄彰任会长（前排居中），基金会成员与彭旧金山总领事合影",
      'image': ["image/alumni_activities/2017_admin.jpg"]
    }, 
    {
      'title': "2007年时任武汉市委书记（现任工信部部长）苗圩-左三与基金会部分成员（欧阳明-右二，王高峰-右一）合影",
      'image': ["image/alumni_activities/2007_wuhan_maire.jpg"]
    }, 
    {
      'title': "2007年 刘经南 校长访问基金会留影",
      'image': ["image/alumni_activities/2007_president.jpg"]
    }, 
    {
      'title': "2006年 校友会校友年度BBQ",
      'image': ["image/alumni_activities/2006_bbq.jpg"]
    }, 
    {
      'title': "2005年宁挺，欧阳明，王高峰等代表基金会参与华人运动会",
      'image': ["image/alumni_activities/2005_sport_meet.jpg"]
    }, 
    {
      'title': "1998年校友会成立大会合影留念",
      'image': ["image/alumni_activities/1998_setup.jpg"]
    }
  ]
}

alumni_activities_info = {
        'home_images': ["image/alumni_activities/2018_bbq.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_activities/2017_bbq.jpg", "image/alumni_activities/2017_admin.jpg", \
                "image/alumni_activities/2018_prof.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_activities/2007_president.jpg"  ],

        'introduction': [
            "武汉大学北加州校友会成立伊始，就本着团结武汉海外校友，凝聚武大海外力量，扩大武大海外影响力，连接武大与美国加州的目的，组织了一系列社交，学术，交流，对接等活动，获得校友的大力支持和武汉大学，武汉大学校友总会的认可和肯定。校友活动包括一年一度的校友新春联欢，年度中秋BBQ聚会，武汉大学代表团接待，武汉大学学生海外游学团接待，并积极参与旧金山总领事管组织的新春团拜，跨校友会合作等活动。在祖国需要海外支援时，包括2003年非典疫情，2008年汶川地震等积极募捐资金和物资支援祖国。",
            "对于此次爆发于武汉的2019-nCoV疫情，校友更是十分牵挂母校和武汉疫情防控，在第一时间校友会开展募捐资金和紧缺医疗物资支援行动，团结广大的北加州校友和北美校友，协调广泛的校友力量，社会力量和美国民间力量，及时协调筹集了大批物资送到一线医护人员手上，更多的校友会支援武汉行动依然在进行。",
            "众志成城，抗击疫情，校友会在行动！武汉加油，中国加油！"
            ],


        'activites_info': [
            {
                'title': "2019年10月 校友会年度BBQ (拔河掠影)",
                'image': ["image/alumni_activities/2019_bbq_1.jpg", "image/alumni_activities/2019_bbq_2.jpg"]
                }, 
            {
                'title': "2019年10月 校友会协办3551国际创业大赛(硅谷赛区)",
                'image': ["image/alumni_activities/2019_3551.jpg"]
                }, 
            {
                'title': "2019年8月校友会对接生命科学院暑期访学团",
                'image': ["image/alumni_activities/2019_life_science_1.jpg", "image/alumni_activities/2019_life_science_2.jpg"]
                }, 
            {
                'title': "2018年12 武大校友同武大院士教授欢聚",
                'image': ["image/alumni_activities/2018_prof.jpg"]
                }, 
            {
                'title': "2018年10月 校友会年度BBQ合影",
                'image': ["image/alumni_activities/2018_bbq.jpg"]
                }, 
            {
                'title': "2018年10月校友会协办3551国际创业大赛(硅谷赛区)",
                'image': ["image/alumni_activities/2018_3551.jpg"]
                }, 
            {
                'title': "2018年8月校友会对接生命科学院暑期访学团",
                'image': ["image/alumni_activities/2018_life_science.jpg"]
                }, 
            {
                'title': "2018年8月校友会代表队参与第16届北加州华人文化体育协会运动大会",
                'image': ["image/alumni_activities/2018_sport_meet_1.jpg", "image/alumni_activities/2018_sport_meet_2.jpg"]
                }, 
            {
                'title': "2018年4月 武大校董喻鹏和新一届校友会成员一起",
                'image': ["image/alumni_activities/2018_university_council.jpg"]
                }, 
            {
                'title': "2017年 窦贤康校长与校友会在斯坦福组织武大海外恳谈会",
                'image': ["image/alumni_activities/2017_president.jpg"]
                }, 
            {
                'title': "2017年武大校友会全体人员",
                'image': ["image/alumni_activities/2017_alumni.jpg"]
                }, 
            {
                'title': "2017年校友会年度BBD(联合兄弟校友会和湖北同乡会)",
                'image': ["image/alumni_activities/2017_bbq.jpg"]
                }, 
            {
                'title': "2015年11月 武汉大学副校长黄泰岩 在湾区招才引智",
                'image': ["image/alumni_activities/2015_vice_president.jpg"]
                }, 
            {
                    'title': "2010年 武大校长刘经南到湾区看望武大校友",
                    'image': ["image/alumni_activities/2010_president.jpg"]
                    }, 
            {
                    'title': "2007年12月 黄彰任会长（前排居中），基金会成员与彭旧金山总领事合影",
                    'image': ["image/alumni_activities/2017_admin.jpg"]
                    }, 
            {
                    'title': "2007年时任武汉市委书记（现任工信部部长）苗圩-左三与基金会部分成员（欧阳明-右二，王高峰-右一）合影",
                    'image': ["image/alumni_activities/2007_wuhan_maire.jpg"]
                    }, 
            {
                    'title': "2007年 刘经南 校长访问基金会留影",
                    'image': ["image/alumni_activities/2007_president.jpg"]
                    }, 
            {
                    'title': "2006年 校友会校友年度BBQ",
                    'image': ["image/alumni_activities/2006_bbq.jpg"]
                    }, 
            {
                    'title': "2005年宁挺，欧阳明，王高峰等代表基金会参与华人运动会",
                    'image': ["image/alumni_activities/2005_sport_meet.jpg"]
                    }, 
            {
                    'title': "1998年校友会成立大会合影留念",
                    'image': ["image/alumni_activities/1998_setup.jpg"]
                    }

            ]
        }

report_info = {
        'introduction': "武汉市，一个人口1100万的城市，中国中部最大的都市。 2019年12月，武汉地区发现了一种新的冠状病毒。为了限制病毒传播，整座城市正处于封锁状态。到目前为止，该病毒已影响数万名武汉居民，并造成数千人死亡。 \
                武汉处于紧急状态。武汉需要您的帮助。\
                我们正在努力支持武汉的医疗物资，并提供对该疾病的报道和认识。"}
# information about wuhan situation pages
wuhan_situation_info = {
  'introduction': "武汉市，一个人口1100万的城市，中国中部最大的都市。 2019年12月，武汉地区发现了一种新的冠状病毒。为了限制病毒传播，整座城市正处于封锁状态。到目前为止，该病毒已影响数万名武汉居民，并造成数千人死亡。 \
                  武汉处于紧急状态。武汉需要您的帮助。\
                  我们正在努力支持武汉的医疗物资，并提供对该疾病的报道和认识。",
  'china_update_info': {
    'link': 'image/wuhan_situation/wuhan_update_213.jpg',
    'source': {
      'title': "来源:",
      'content': "新浪新闻",
      'link': "https://news.sina.cn/zt_d/yiqing0121?vt=4&pos=undefined"
    }
  },

  'timeline_info': {
    'link': 'image/wuhan_situation/timeline.jpg',
    'source': {
      'title': "来源:",
      'content': "察网 - 医改正能量",
      'link': "http://www.cwzg.cn/politics/202001/54595.html"
    }
  }


}

# information about alumni action pages
  ##  first tag should be title
  ##  second tag should be paragraph
alumni_action_info = {
  'home_images': ["image/alumni_action/h2.jpg", "image/alumni_action/h4.jpg", "image/alumni_action/h7.jpg"],

  'introduction': [ 
                "2019年年末2019-nCoV疫情在武汉爆发，疫情的动态时刻牵动着校友的心，在了解到一线口罩，手套，防护服等医疗物资短缺的情况，校友会第一时间全力以赴，多渠道开展支援活动，包括校友和社会的资金募捐，采购和运送医疗物资，与美国NGO达成医疗物资合作，在媒体呼吁社会力量关注武汉疫情，鼓励美国民间力量支援武汉疫情防控。",
                "日前为止，武汉大学协同兄弟校友会，武汉大学中国校友会分支，美国NGO，湖北慈善总会等中美校友，社会，政府各界力量，同运送超过5.2吨紧急医疗物资到武汉协和医院，中南医院和孝感中心医院一线医护人员手中，包括23.7万医用口罩，5.75万医用口罩，1.3万医用防护服等，更多的校友会支援武汉行动依然在进行。",
                "众志成城，抗击疫情，校友会在行动！武汉加油，中国加油！"
      ],

  'notices': [
      # notice start
        {
        'title_info': {
              'title': "武大华科北加州校友会对Wuhan United 非营利组织正式注册成立的说明",
              'paragraph': "Wuhan United非营利组织正式注册成立，这个新的组织将继续以武大和华科北加州校友会为基础，长期持续的执行募集物资、支援疫区及未来灾区重建的任务。同时，新成立的Wuhan United将面向未来，逐步过渡到独立于两校友会的专业运营模式，并着力于融合更多的力量与资源，更有效的支援疫区。新的组织已建立独立的基金和募资渠道，武大华科校友会将停止已有募资活动，转而全力支持新成立的Wuhan United。为保证新组织的财政清晰和独立，之前募集的资金不会进入新的非营利组织。"
        }, 
        'content_info': [
          {
            'sub_title': "我们的故事"
          },
          {
            'paragraph': "不到一周时间内，北京时间2月3日，Direct Relief（国际直接救济组织）捐赠的第二批医疗物资，包括3万7千只口罩，9千件防护服，5万只手套，在华科武大北加州校友会的协调帮助下，正式送达武汉周边城市——孝感市中心医院。"
          },
          {
            'paragraph': "“我们保护武汉，请求你们支援我们！”"
          },
          {
            'paragraph': "2020年1月29日，一则武汉协和医院宣布物资告急的消息牵动了北加州武大和华科校友们的心。我们能不能利用海外华人的力量，在最快时间内筹措到亟需的医疗物资送到协和医院医务工作人员的手中？"
          },
          {
            'paragraph': "这就是Wuhan United行动最简单的初衷。"
          },
          {
            'paragraph': "Wuhan United最初是由华科88级校友龚义涛师兄联合武汉大学与华中科技大学两个北加校友会共同发起，由三十多位心系家乡的热血青年组成的志愿者队伍。从2020年1月23日，武汉宣布全面封城伊始，这18天以来，我们的志愿者在完成自己的本职工作之余，几乎把所有的空余时间都奉献给支援国内抗击新型冠状病毒第一线。许多志愿者更是在爆肝工作，连续十几个日日夜夜，每天只休息三四个小时。"
          },
          {
            'sub_title': "我们的行动"
          },
          {
            'paragraph': "在深知国内医疗物资极度紧缺的情况下，Wuhan United立即开展了将急需物资直接运往一线医院的工作。然而团队很快发现直接购买大量医疗物资现货非常困难，并且意识到大型国际非营利组织 (NPO) 的医疗物资储备可以第一时间用于灾区"
          },
          {
            'paragraph': "于是，Wuhan United联系到了国际救援组织Direct Relief，为武汉协和医院申请到第一批救急的医疗物资。在武大华科校友会、美国联邦快递、中国邮政的协作下，Wuhan United团队在36小时内顺利打通了运输途中的清关、装卸货、货物运输与跟踪，又通过两校在各地的校友会完成武汉、孝感、黄冈等地的地接任务，保证了物资顺利、准时到达。"
          },
          {
            'paragraph': "十几天以来的高负荷工作，Wuhan United为Direct Relief等NPO与疫情重灾区的前线医院之间构筑了一道直通的桥梁，并且多次协调帮助Direct Relief成功直送亟需的医疗物资，进入国内抗击新型冠状病毒的一线。"
          },
          {
            'paragraph': "2020年1月31日，Direct Relief第一批共计17个托盘2.5吨重的医疗物资在武汉协和医院告急的时刻直接到达，其中包括20万个医用外科口罩、2.75万双医用手套及4000件防护服。也是这次捐助把我们送上了微博热搜。"
          },
          {
            'paragraph': "2020年2月3日，Direct Relief第二批共计20个托盘2.7吨重的医疗物资送达孝感市中心医院，其中包括3万7千只口罩，9千件防护服，5万只手套。"
          },
          {
            'paragraph': "2020年2月6日-7日，Direct Relief第三批共计77个托盘10吨重的医疗物资离开位于加州的仓库，分批前往武汉市同济医院、黄冈市黄州总医院、孝感市中心医院以及重庆市慈善总会，其中包括25万个N95口罩，34万个医用手套以及鞋套，防护服，隔离衣等。"
          },
          {
            'paragraph': "2020年2月7日，Wuhan United、Direct Relief、Fedex三方共同协助总部位于Connecticut的跨国公司Amphenol捐赠5个托盘的医疗物资，出发前往武汉市同济医院，其中包括1万多件隔离服、面罩等。"
          },
          {
            'paragraph': "同期，Wuhan United和另外一个国际非营利救援组织MAP International也建立了合作关系，由MAP牵头，Wuhan United 以及其他捐赠机构共同捐助的超过134万个口罩，1万件防护服，还有28万双手套正在运往湖北疫区。"
          },
          {
            'sub_title': "我们和Wuhan United（新成立的NPO）的关系"
          },
          {
            'paragraph': "现在，这个行动将通过新成立的组织Wuhan United继续下去。两个校友会意识到抗击疫情、助力疫情灾后重建是一个长期的、艰巨的任务，也需要聚集更多各方面的资源和力量，这不是以校友会现有组织架构能够完全做到的。我们需要一个更专业，更专注的组织来继续完成这项有意义的工作。于是，经Wuhan United执行团队的斟酌，与两大校友会共议后，新成立的Wuhan United 正式注册为501(c)(3) 非营利组织（NPO），并由龚义涛师兄担任首任President。我们认为这个新平台将凝聚更多的资源、汇聚各界的力量，将之前的工作更高效地开展下去。"
          },
          {
            'paragraph': "新成立的Wuhan United以NPO的身份继续运作后，两大校友会仍然是中坚力量。目前的志愿者团队将继续在Wuhan United旗帜下向前推进，我们拥有共同的目标、协作的默契，可以用最高效的方式继续为疫区做贡献。同时校友会也会逐渐退入幕后，让Wuhan United独立成长，融合更多的资源和力量。"
          },
          {
            'paragraph': "为了确保过渡顺利，武大和华科北加校友会各委派一个代表加入Wuhan United理事会担任理事。待过渡顺利完成后，武大和华科代表会退出Wuhan United理事会。但无论是何种身份，两个校友会以及现有的志愿者团队今后仍会在Wuhan United的旗帜下继续努力，支持Wuhan United的抗疫救灾活动。"
          },
          {
            'paragraph': "此外，为了保证新成立的NPO财政清晰、财务独立、避免误会，武大海外校友科学基金会和华科硅谷基金会之前及以后所募得资金不会进入新成立的Wuhan United NPO。"
          },
          {
            'sub_title': "我们募集资金的说明"
          },
          {
            'paragraph': "武汉大学海外校友基金会已于美国西部时间2020年2月5日中午12点停止为Wuhan United接受捐款。华科硅谷基金会将于2020年2月10日凌晨停止为Wuhan United接受捐款。"
          },
          {
            'paragraph': "截止2020年2月9日凌晨，武汉大学海外校友科学基金会和华科硅谷基金会总共募集了33万余美元。两校友会基金会募集的资金大部分已经承诺直接捐赠给两个非盈利组织Direct Relief和MAP International，以支持他们继续向疫区支援，并会在捐款平台资金到账后立即捐出。剩余的资金也将全部捐赠给其他支援疫区和灾区重建的项目或组织。"
          },
          {
            'paragraph': "同时，鉴于捐款可能存在滞后性，两个基金会承诺，将其2020年6月30日前收到的所有捐赠，若无特别说明，全部视为支持疫区的捐款，并会用于上述支援疫区的用途。两基金会所有善款使用将会详细公示，并且不会进入新成立的Wuhan United NPO。"
          },
          {
            'paragraph': "从2020年2月10日凌晨起，新成立的Wuhan United NPO将正式开始接受捐赠。关于Wuhan United的运作、募捐机制及资金分配详细情况，请关注Wuhan United的公众号或网站更新。"
          },
          {
            'sub_title': "我们和WUHAN UNITED在一起"
          },
          {
            'paragraph': "“聚是一团火，散作满天星。” 我们华科和武大的志愿者队伍将在Wuhan United NPO的组织下继续努力，护卫家乡。我们两个校友会的会长巨辉、粟海也会在新的NPO内担任董事。如果你也与我们有着相同的愿景，欢迎加入Wuhan Untied的志愿者团队。让我们一起努力，为疫区祈福，为医护人员助力，为还原我们心中的武汉而奋斗。"
          },
          {
            'paragraph': "更多信息，请关注Wuhan United的网站（www.wuhanunited.org）、微博wuhanunited和微信公众号 "
          },
          {
            'paragraph': "如果您想加入Wuhan United团队，或是贡献自己一份力量，请联系info@wuhanunited.org"
          }
        ]
      },



      # notice end


      # notice start
        {
        'title_info': {
              'title': "DR捐赠2.7吨医疗物资，与武大华科北加校友会二度联手完成跨洋援助至孝感",
              'paragraph': "关注本公号的各位读者都知道，在1月31日，由Direct Relief（国际直接救济组织）捐赠重达2.5吨驰援武汉的应急医疗物资从旧金山飞跃太平洋，顺利抵达武汉协和医院，由武汉加油行动武汉分队的志愿者亲手交付到医护工作者手中，其中包括目前急需的20万支医用外科口罩、2.75万双医用手套及4000件防护服。"
        }, 
        'content_info': [
          {
            'paragraph': "不到一周时间内，北京时间2月3日，Direct Relief（国际直接救济组织）捐赠的第二批医疗物资，包括3万7千只口罩，9千件防护服，5万只手套，在华科武大北加州校友会的协调帮助下，正式送达武汉周边城市——孝感市中心医院。"
          },
          {
            'paragraph': "这也是Wuhan United（华科武大北加州校友会）与Direct Relief（国际直接救济组织）的再度合作，将捐赠方Direct Relief的第二批援助医疗物资成功交付孝感市中心医院。"
          },
          {
            'paragraph': "Direct Relief（国际直接救济组织）是美国最大的国际非政府组织之一，活跃在全美50个州以及全世界90多个国家。在向武汉协和医院捐赠了包括20万个医用口罩在内的第一批医疗物资后，Direct Relief再一次雪中送碳，捐助了20个托盘的物资给湖北其他地区的一线医院，这其中包括：3万7千只口罩，9千件防护服，5万只手套等。"
          },
          {
            'paragraph': "Wuhan United在其中承担了包括医院和捐赠方对接、文本、清关、物流支持等组织协调工作，确保这批从加州起飞的物资能顺利、直接抵达孝感市中心医院。"
          },
          {
            'paragraph': "与上次行动一致的是，本次援助行动的国际段运输仍由美国联邦快递（Fedex）承运，物资在广州清关后，由中国邮政EMS直接发往孝感。"
          },
          {
            'paragraph': "孝感位于湖北省东北部，与武汉接壤，距离武汉市中心只有60公里，是武汉市流动人口最主要的目的地之一。截止小编发稿时为止，孝感市新型冠状病毒感染的肺炎病例已达1120例，是除武汉市、黄冈市以外感染病例最多的城市。"
          },
          {
            'paragraph': "孝感市中心医院是当地的三甲医院，自肺炎疫情发生以来一直是发热门诊、医疗救治定点医院，同样面临着医疗物资紧缺的状况。孝感市中心医院早于1月26日就发出了接受社会爱心捐赠的公告。希望这批来自Direct Relief的物资能够缓和目前医疗资源短缺的状况，帮助湖北省除武汉市以外的地级市、县级市共同抗击肺炎疫情。"
          },
          {
            'paragraph': "从Wuhan United成立开始，与非政府组织合作、将最急需的医疗物资直接送到一线医院一直是我们的工作重心。面对疫情仍处在扩散阶段的严峻形势，我们团队会深入与Direct Relief的合作关系，同时诚挚邀请更多的非政府组织和跨国企业加入。"
          },
          {
            'paragraph': "在成功驰援武汉、孝感医院后，我们会继续与非政府组织和跨国企业合作，努力将更多医疗物资送到武汉及周边地区，为打赢这场抗疫攻坚战增添一份助力。"
          },
          {
            'sub_title': "本次援助任务特别致谢"
          },
          {
            'list': [
                        '湖北慈善总会', '联邦快递', '广东邮政', '华科北加州校友会', '武大北加州校友会', '华科武汉校友会'
                    ]
          },
          {
            'sub_title': "欢迎更多的非政府组织和跨国企业与我们联系，联系方式"
          },
          {
            'paragraph': "Wuhan United官网：www.wuhanunited.org"
          },
          {
            'paragraph': "新浪微博，请搜：wuhanunited"
          },
          {
            'paragraph': "媒体联系邮箱：Sunny Sun, media@wuhanunited.org"
          }
        ] # content_info end 
      },
      # notice end

      # notice start
      {
        'title_info': {
              'title': "21小时接力护送！2.5吨医用物资从旧金山直接运抵武汉协和医院",
              'paragraph': "人民网旧金山1月31日电（记者邓圩）21小时接力护送！北京时间1月31日下午，由WuhanUnited(武大和华科北加州校友会）联合国际直接援助组织(Direct Relief)捐赠的2.75万双医用手套，4000件隔离服，20万个外科手术口罩，重达2.5吨货物从旧金山直接运抵武汉协和医院。",
              # 'image': {
              #    'link': "image/alumni_action/h1.jpg",
              #    'title': "协和医院和武大中南医院接受捐赠物资"
              # }
          }, 
        
        'content_info': [
          {
            'sub_title': "“武汉加油” 北加州在行动"
          },
          {
            'paragraph': "武汉加油行动（Wuhan United）是一支心系湖北的在美华人组成的志愿者团队。行动的发起者是旧金山湾区的武汉大学北加州校友会和华科北加州校友会，包括硅谷高科技公司工程师、大学教授及医疗工作者等多个领域的专业人士。对这些曾就学于武汉的莘莘学子，武汉对于每一个成员来说都有如家一般的存在。"
          },
          {
            'paragraph': "区别于购买市面上散货的方式，武汉加油行动团队成立之初，一直在寻求与非政府组织合作的机会。他们与Direct Relief（国际直接援助组织）与达成战略合作，搭建了一座跨国桥梁，将非政府组织所拥有的医疗捐赠物资直接送达武汉抗击疫情一线。"
          },
          {
            'sub_title': "货车开往机场路上还在完成通关手续"
          },
          {
            'paragraph': "货车开往机场路上还在完成通关手续"
          },
          {
            'paragraph': "21小时完成不可能的任务，背后是与时间赛跑的故事。"
          },
          {
            'paragraph': "美西时间与北京时间有16小时时差。从志愿者团队与Direct Relief最终达成合作，到物流飞机起飞，仅仅剩下一个周日和半个工作日。"
          },
          {
            'paragraph': "旧金山当地时间1月27日下午3点，救助武汉协和医院的物资离开仓库，前往机场，这个时间在中国还是半夜。团队需要完成捐赠方、承运方、接收方、海关清关以及报关公司5个单位所有的文书材料，无疑是与时间赛跑。"
          },
          {
            'paragraph': "捐赠物资的海关手续，在货车开往机场和飞机飞越太平洋的途中，在中美两地紧锣密鼓地进行着。"
          },
          {
            'paragraph': "美西时间1月28日，北京时间1月29日凌晨，运送物资的飞机抵达广州,完成清关手续抵达中国邮政广州转运中心，由武汉大学广州校友会全程护送，当晚10点中国邮政EMS货车启程武汉。"
          },                      
          {
            'source': {
                'title': "来源: ",
                'content': "人民网-国际频道",
                'link': "http://world.people.com.cn/n1/2020/0201/c1002-31566128.html",
            }
          }
        ] # content_info end 
      } # notice end
    ] # notices end 
}

# information about donate pages
donate_info = {
        # dynamic create page info
        # tag: title, sub_title, paragraph, table, image, source, list

        # first notice
        'notices': [

            # notice start
            [   
                {
                  'sub_title': "行动发起方"
                },
                {
                  'paragraph': "作为众多身在硅谷的海外华人之一，华科、武大、浙大三校硅谷校友会决定共同携手，发起此次“CARE”行动，为我们生活的社区、家园，群策群力，打赢这场新冠病毒战役，我们也欢迎各界朋友加入。"
                },
                {
                  'paragraph': "主办单位：华中科技大学、武汉大学、浙江大学硅谷校友会"
                },
                {
                  'paragraph': "联合主办单位：加州湖北同乡总会"
                },

                {
                  'sub_title': "捐款去向"
                },
                {
                  'paragraph': "此次“CARE”行动，募捐将分两大主要去向："
                },
                {
                  'paragraph': "第一，对医务人员个人防护设备（PPE）的捐助。我们将根据美国各大媒体、政府机构等发布经核实的信息，针对具体需要，对医疗机构进行资金及物资的专向捐赠。"
                },
                {
                  'paragraph': "第二，为社区提供公共服务群体的捐助。随着“居家隔离令”（Shelter-in-Place）的发布，越来越多人在家工作，但公共部门如卫生部门、警察局、消防局，超市、快递、餐饮等“必需行业”的工作人员依旧为本地居民服务着，这些行业服务人员的个人防护也是关注重点。"
                },
                {
                  'paragraph': "无论是医护人员，还是快递小哥，帮助他们，保护好他们，就是保护好我们自己，保护好我们的社区。"
                },

                {
                  'sub_title': "募捐账户"
                },
                {
                  'paragraph': "募捐账户如下："
                },
                {
                    'source': {
                        'title': "Paypal（Recipient：Zheda Alumni Foundation）：",
                        'content': 'https://tinyurl.com/zheda501c3',
                        'link': 'https://tinyurl.com/zheda501c3'
                        }
                },
                {
                  'paragraph': "或可扫描下方二维码"
                },
                { 'image': {
                    'link': "../upload/ID9_donate_1.jpg",
                    'title': ""
                    }
                },
                {
                  'paragraph': "Benevity：Zheda Alumni Foundation 可在公司捐款平台搜索到，欢迎公司有“match fund” 的校友和朋友积极参与。"
                },
                {
                    'source': {
                        'title': "欢迎点击 ",
                        'content': 'https://tinyurl.com/zheda501c3-COVID19',
                        'link': 'https://tinyurl.com/zheda501c3-COVID19'
                        }
                },
                {
                  'paragraph': "或扫描下方二维码填写登记表，以便我们表示感谢。"
                },
                { 'image': {
                    'link': "../upload/ID9_donate_2.jpg",
                    'title': ""
                    }
                },

                {
                  'sub_title': 'Q&A'
                },
                {
                  'paragraph': 'Q：本次捐款活动如何保证公开透明?'
                },
                {
                  'paragraph': 'A：本次捐款将会及时通过微信公众号进行募捐数额、购买、募集物资、送达结果的公布。我们将保证募捐过程的公开透明，欢迎大家监督。'
                },
                {
                  'paragraph': 'Q：本次捐款的物资如何保证及时送达？'
                },
                {
                  'paragraph': 'A：每次捐款，或者采购的物资将会根据接收方的需求、紧急程度进行第一时间派送，更多现场将会通过公众号进行更新。'
                },
                {
                  'paragraph': 'Q：个人或企业能否通过我们的行动进行医疗物品的捐赠？'
                },
                {
                  'paragraph': 'A：如果您有符合FDA医疗标准，且有现货可进行及时捐赠的大宗PPE物资，欢迎通过后台留言联系我们。'
                },
                {
                  'paragraph': 'Q：是否可以提供税收减免收据？'
                },
                {
                  'paragraph': 'A：我们的捐款渠道都是501(c)(3)注册的NGO。捐款都是100%税务减免。'
                },
                {
                  'paragraph': 'Q：我不是三校校友，是否可以参与这次募捐？'
                },
                {
                  'paragraph': 'A：无论你是三校校友，还是热心的华人志愿者，只要你愿意服务和帮助我们的社区，欢迎你进行募捐，加入我们的战疫行动，帮助我们所处的社区更快战胜疫情！欢迎各公司、组织参与捐款。'
                },
                {
                  'paragraph': '如果您有志于参与硅谷线下物资的捐赠、派送，和采购，欢迎联系我们！'
                },
                {
                  'paragraph': '最后，请各位校友和朋友们遵照加州和湾区县市公共卫生部门的“居家隔离”要求，保重身体，保持良好心态，关心他人。'
                },


                # {
                #   'source': {
                #     'title': "Paypal：",
                #     'content': "https://tinyurl.com/zheda501c3",
                #     'link': "https://tinyurl.com/zheda501c3"
                #   }
                # },
                # {
                #   'paragraph': "（Recipient：Zheda Alumni Foundation）可扫描下方二维码"
                # },

                # {
                #     'title': "财务公示和募捐计划重要更新 (2月3日)"
                #     },
                # {
                #     'sub_title': "财务信息公示"
                #     },
                # {
                #     'paragraph': "非常感谢热心支援新冠状病毒疫区的各位捐赠人。截止于美国西部时间2月2日（募款第5天）0时，Wuhan United筹集到的资金总额为$240,273。这些资金将陆续从各个捐助平台转入为Wuhan United募捐的武大海外校友科学基金会和华科硅谷基金会。各主要平台具体捐赠情况如下："
                #     },
                # {
                #     'table': [
                #         "|GoFundMe|Benevity(incl employer match)|Paypal",
                #         "武大海外校友科学基金会|$138,308.00|$32,374.64|$17,302.36",
                #         "华科硅谷基金会|NA|$22,214.00|30,074.00"
                #         ]
                #     },
                # {
                #     'paragraph': "Wuhan United执委会自2020年1月23日成立以来，就设立了一个急迫的工作目标： 迅速筹集国内医院急需的医用物资， 并将筹集到的物资运送到疫区一线医院。"
                #     },
                # {
                #     'paragraph': "为实现这个目标，Wuhan United 执委会从1月23日起就组建专业人士团队寻找大批量的急需医用物资，如N95口罩，防护服等。然而很快发现市场上极难找到符合标准的可靠现货货源。由于捐款平台的运作方式，我们预计到2月中下旬才能得到捐款平台的支付。这样的现金流也是无法大批量及时地购买武汉所急需的物资的。为此我们的团队在摸索几天时间后做出决定，并在极短的时间内与美国大型NGO建立合作，争取捐助意向，帮助他们与疫区医院对接，确定援助物资，并帮助他们完成运输物资所需要的所有文件，协调运输通关，以及通过国内热心校友与志愿者们保驾护航，确保物资快速顺利到达指定医院。1月31日在武汉协和医院物资告急的时刻，终于将第一批Direct Relief捐赠的2.5吨医疗物资直接送达！详细报道请参考公众号前文，及全程录像"
                #     },
                # {
                #     'source': {
                #         'title': "",
                #         'content': 'https://www.youtube.com/watch?v=6SqgCPgioVE',
                #         'link': 'https://www.youtube.com/watch?v=6SqgCPgioVE'
                #         }
                #     },
                # {
                #     'paragraph': '除了与Direct Relief进行合作，我们也和MAP International建立了合作伙伴关系。我们承诺将部分捐款用于支持他们。由MAP International牵头，Wuhan United 以及其他捐赠机构共同捐助的超过134万个口罩，1万件防护服，还有28万双手套将发往湖北疫区。具体报道请参考'
                #     },
                # {
                #     'source': {
                #         'title': "",
                #         'content': 'https://sites.google.com/view/wuhan-ncov-crisis-fundraise/our-work/wuhan-united-partnered-with-map-international',
                #         'link': 'https://sites.google.com/view/wuhan-ncov-crisis-fundraise/our-work/wuhan-united-partnered-with-map-international'
                #         },
                #     },
                # {
                #     'source': {
                #         'title': "",
                #         'content': 'https://www.map.org/media',
                #         'link': 'https://www.map.org/media'
                #         },
                #     },
                # {
                #     'paragraph': '今后短期内Wuhan United的工作重心将以这种模式继续与拥有稳定货源的大型NGO合作，促进更多的医疗资源迅速支援疫区。募集的资金一部分将用于深化与NGO的合作，以支持他们对疫区的贡献。疫区的情况每天都在变，我们的工作也会根据情况进行调整，一定尽我们所能为疫区做更多的事情。我们重申，所有募集到的资金都将用于支援疫区的工作中。谢谢大家的支持！'
                #     },
                # {
                #         'sub_title': '重要更新声明'
                #         },
                # {
                #         'paragraph': '基于目前通过武汉大学海外校友科学基金会善款捐赠的数额已经达到我们预先设定的范围，经Wuhan United执委会、武汉大学海外校友科学基金会和华科校友基金会商讨决定，武汉大学海外校友科学基金会将逐步停止受理对Wuhan United行动的捐赠，具体方式如下：'
                #         },
                # {
                #         'list': [ '武汉大学海外校友基金会将会在美国西部时间2020年2月5日中午12时，停止代理接收针对Wuhan United的资金捐赠。同时，以免热心的朋友没有及时看到这一条消息，武汉大学海外校友基金会将把于美国西部时间2020年6月30日中午12时之前所有对武汉大学海外校友基金会的捐赠，用于支持Wuhan United，支持武汉，支持湖北，抗击新冠疫情。',
                #             '华科校友基金会将继续为Wuhan United行动募集资金。',
                #             '华科及武大北加州校友会的志愿者们将继续全力支持Wuhan United的后续支援行动'
                #             ],
                #         },
                # {
                #         'sub_title': 'Q&A'
                #         },
                # {
                #         'paragraph': 'Q：目前已有哪些NGO合作对象'
                #         },
                # {
                #         'paragraph': 'A：我们已经和Direct Relief和MAP International建立了合作关系。同时我们也在积极寻求更多NGO的合作机会。'
                #         },
                # {
                #         'paragraph': 'Q：资金去向'
                #         },
                # {
                #         'paragraph': 'A：已经募集的资金一部分将用于深化与NGO的合作，以支持他们对疫区的贡献。疫区的情况每天都在变，我们的工作也会根据情况进行调整，一定尽我们所能为疫区做更多的事情。我们重申，所有募集到的资金都将用于支援疫区的工作中。'
                #         },
                # {
                #         'paragraph': 'Q：如何确保这些NGO的资金和物资能够用到中国疫情中'
                #         },
                # {
                #         'paragraph': 'A：我们会以各种方式参与NGO的关于疫情捐赠事宜，从争取捐助意向，帮助他们与疫区医院对接，确定援助物资，帮助他们完成运输物资所需要的所有文件，协调运输通关，以及通过国内热心校友与志愿者们保驾护航，确保物资快速顺利到达指定医院。'
                #         },
                # {
                #         'paragraph': 'Q：捐款平台会有手续费吗'
                #         },
                # {
                #         'paragraph': 'A：”The GoFundMe platform is free. A standard transaction fee of 2.9% plus $0.30 per donation allows for credit card processing and safe transfer of funds.” (Quoted from Gofundme FAQ)； PayPal有募捐手续费每笔2.2%或2.9%+$0.30'
                #         },
                # {
                #         'paragraph': 'Q：各个账户多久可以到账'
                #         },
                # {
                #         'paragraph': 'A：Gofundme：“All donations are made directly to PayPal Giving Fund (a 501(c)(3) charitable organization). After the deduction of payment processing fees, PayPal Giving Fund delivers the funds they receive on a monthly basis. Payment processing fees including PayPal‘s transaction fee and GoFundMe’s processing cost for the secure transfer of funds. PayPal Giving Fund does not charge a fee for its services.” (Quote from Gofundme policies)； Benevity 账期至少为1个月'
                #         },
                # {
                #         'paragraph': 'Q：我们如何知道捐款情况的更新'
                #         },
                # {
                #         'paragraph': 'A：每周会在网站和公众号上更新募捐情况与工作进展。'
                #         }
                ]
        # notice end
    ]
}

# information about contact。
contact_us_info = {

        }

# information about qa pages
qa_info = {
  'title': '常见问题',

  'questions': [
    {'q': '如何加入武汉大学北加州校友会网络？', 'a': '请加微信：chenwang890101，验证校友身份后，邀请加入校友会微信群。'},
    {'q': '校友会是否接受小批量物资捐赠？', 'a': '目前校友会暂无渠道处理小批量散货的援助，专注大批量物资的集中运输，但是校友会可以协调关联其他平台处理散货援助，请加校友会微信.'},
    {'q': '现在中美航班停飞，会影响校友会运输物资回国么？', 'a': '我们是和美国慈善组织合作来向中国捐助物资，是以货运包机的形式，民航停飞对我们目前没有影响。'},
    {'q': '现阶段捐款收入支出会向社会公布么？', 'a': '我们将会在网站上公开账目和去向，目前正在处理网站公示的技术问题。'},
    {'q': '本次募集采购的器材是什么？', 'a': '校友会将采购的四类器材，根据武汉协和医院官方捐赠要求：防护口罩包括：医用防护口罩：符合中国GB 19083-2010 N95口罩：美国NIOSH认证，非油性颗粒物过滤效率 >=95% 欧洲N95口罩：欧洲FFP2标准 KN95口罩：符合中国GB 2626强制性标准，非油性颗粒物过滤效率 >=95%。这些口罩不带呼吸器/呼吸阀的外科口罩：符合 yy 0469-2011医用外科口罩防护服：符合GB19082-2009《医用一次性防护服技术要求》二级以上医用防护服：一般衣服上有红蓝条纹护目镜：二级以上医用护目镜。'},
    {'q': '如何保证医疗物资及资金可以递送到湖北的医院？','a': '当下武汉的疫情防控政策每日都在更新，随时可能放宽或收紧。我们将遵从“专款专用，扶助医护”的原则，力图用最有效最可靠的途径将物资运送到疫情战斗的一线。'},
    {'q': '捐款购买的医疗物资是否会送达指定医院或者武汉周边城市？', 'a': '校友会将秉承“同舟共济，情系家乡”的精神，在捐款过程中即时会通过网站及微信公众号，更新募捐数额、购买募集产品种类及数量、送达结果。我们将保证募捐的公开透明，也欢迎大家监督。'},
    {'q': '是否可以提供税收减免收据？', 'a': '我们的捐款渠道都是501(c)(3)注册的NGO。捐款都是100%税务减免。'}
  ]
}

# pass page info to correct page
menus2page = {
        'index': index_info,
        'alumni_activities': alumni_activities_info,
        'wuhan_situation': wuhan_situation_info,
        'report': report_info,
        'alumni_action': alumni_action_info,
        'donate': donate_info,
        'contact_us': contact_us_info,
        'qa': qa_info
        }


# dynamic notices
notices = [
        # {
        #   "title": "第二批物资已于美国时间1月28日凌晨从纽约起飞......",
        #   "content": "第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......",
        #   "source": "武大校友会",
        #   "date": '2020',
        #   "type": '捐赠',
        #   "tag": '物资',
        #   "status": 'active'
        # },
        # {
        #   "title": "第一批物资已于美国时间1月27日凌晨从纽约起飞......",
        #   "content": "第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......",
        #   "source": "武大校友会",
        #   "date": '2020',
        #   "type": '捐赠',
        #   "tag": '物资',
        #   "status": 'active'
        # },
        ]
