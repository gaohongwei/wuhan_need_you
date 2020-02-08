# coding: utf-8

# dynamic create menu
menus = [
	 {
	    'label': "主页",
	    'path': '/index'
  	},
  	{
    	'label': "校友活动",
    	'path': '/alumni_activities'
  	},
  	{
	    'label': "武汉疫情动态",
	    'path': '/wuhan_situation'
  	},
  	{
	    'label': "校友会在行动",
	    'path': '/alumni_action'
  	},
  	{
	    'label': "捐赠方式和公示",
	    'path': '/donate'
  	},
  	{
	    'label': "联系我们",
	    'path': '/contact_us'
  	},
  	{
	    'label': "Q&A",
	    'path': '/qa'
  	},
]

# information about index pages
index_info = {

    'home_images': ["image/alumni_activities/2018_bbq.jpg", "image/alumni_activities/2017_president.jpg", "image/alumni_action/h2.jpg", "image/alumni_action/h6.jpg"],

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
      'image': "image/alumni_activities/1998_setup.jpg",
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

# information about wuhan situation pages
wuhan_situation_info = {
  'introduction': "武汉市，一个人口1100万的城市，中国中部最大的都市。 2019年12月，武汉地区发现了一种新的冠状病毒。为了限制病毒传播，整座城市正处于封锁状态。到目前为止，该病毒已影响数千名武汉居民，并造成数百人死亡。 \
                  武汉处于紧急状态。武汉需要您的帮助。\
                  我们正在努力支持武汉的医疗物资，并提供对该疾病的报道和认识。",
  'china_update_info': {
    'link': 'image/wuhan_situation/wuhan_update_203.jpg',
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
      [
        {
          'title': "DR捐赠2.7吨医疗物资，与武大华科北加校友会二度联手完成跨洋援助至孝感"
        },
        
        {
          'paragraph': "关注本公号的各位读者都知道，在1月31日，由Direct Relief（国际直接救济组织）捐赠重达2.5吨驰援武汉的应急医疗物资从旧金山飞跃太平洋，顺利抵达武汉协和医院，由武汉加油行动武汉分队的志愿者亲手交付到医护工作者手中，其中包括目前急需的20万支医用外科口罩、2.75万双医用手套及4000件防护服。"
        },
        {
          'paragraph': "不到一周时间内，北京时间2月3日，Direct Relief（国际直接救济组织）捐赠的第二批医疗物资，包括3万7千只口罩，9千件防护服，5万只手套，在华科武大北加州校友会的协调帮助下，正式送达武汉周边城市——孝感市中心医院。"
        },
        # {
        #   'image': {
        #       'link': "image/alumni_action/news2_1.jpg",
        #       'title': "图注：在加州仓库，华科校友帮助打印了汉语标签"
        #     }
        # },
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
        # {
        #   'image': {
        #       'link': "image/alumni_action/news2_2.jpg",
        #       'title': "数据来源：湖北省卫健委 截至2020年2月3日"
        #     }
        # },
        {
          'paragraph': "孝感市中心医院是当地的三甲医院，自肺炎疫情发生以来一直是发热门诊、医疗救治定点医院，同样面临着医疗物资紧缺的状况。孝感市中心医院早于1月26日就发出了接受社会爱心捐赠的公告。希望这批来自Direct Relief的物资能够缓和目前医疗资源短缺的状况，帮助湖北省除武汉市以外的地级市、县级市共同抗击肺炎疫情。"
        },
        # {
        #   'image': {
        #       'link': "image/alumni_action/news2_3.jpg",
        #       'title': "图注：孝感中心医院物资停留在广州，转运中"
        #     }
        # },
        # {
        #   'image': {
        #       'link': "image/alumni_action/news2_4.jpg",
        #       'title': "图注：孝感中心医院接受Direct Relief物资，华科武大北加州校友会共同协助地接"
        #     }
        # },
        # {
        #   'image': {
        #       'link': "image/alumni_action/news2_5.jpg",
        #       'title': "图注：孝感中心医院接受Direct Relief物资"
        #     }
        # },
        # {
        #   'image': {
        #       'link': "image/alumni_action/news2_6.jpg",
        #       'title': "图注：孝感中心医院接受Direct Relief物资"
        #     }
        # },
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

        
      ],
      # notice end

      # notice start
      [
        {
          'title': "21小时接力护送！2.5吨医用物资从旧金山直接运抵武汉协和医院"
        },
        {
          'paragraph': "人民网旧金山1月31日电（记者邓圩）21小时接力护送！北京时间1月31日下午，由WuhanUnited(武大和华科北加州校友会）联合国际直接援助组织(Direct Relief)捐赠的2.75万双医用手套，4000件隔离服，20万个外科手术口罩，重达2.5吨货物从旧金山直接运抵武汉协和医院。"
        },
        {
          'image': {
             'link': "image/alumni_action/h1.jpg",
             'title': "协和医院和武大中南医院接受捐赠物资"
            }
        },
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
      ]
      # notice end


  ]


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
            'title': "财务公示和募捐计划重要更新 (2月3日)"
          },
          {
            'sub_title': "财务信息公示"
          },
          {
            'paragraph': "非常感谢热心支援新冠状病毒疫区的各位捐赠人。截止于美国西部时间2月2日（募款第5天）0时，Wuhan United筹集到的资金总额为$240,273。这些资金将陆续从各个捐助平台转入为Wuhan United募捐的武大海外校友科学基金会和华科硅谷基金会。各主要平台具体捐赠情况如下："
          },
          {
            'table': [
                  "|GoFundMe|Benevity(incl employer match)|Paypal",
                  "武大海外校友科学基金会|$138,308.00|$32,374.64|$17,302.36",
                  "华科硅谷基金会|NA|$22,214.00|30,074.00"
              ]
          },
          {
            'paragraph': "Wuhan United执委会自2020年1月23日成立以来，就设立了一个急迫的工作目标： 迅速筹集国内医院急需的医用物资， 并将筹集到的物资运送到疫区一线医院。"
          },
          {
            'paragraph': "为实现这个目标，Wuhan United 执委会从1月23日起就组建专业人士团队寻找大批量的急需医用物资，如N95口罩，防护服等。然而很快发现市场上极难找到符合标准的可靠现货货源。由于捐款平台的运作方式，我们预计到2月中下旬才能得到捐款平台的支付。这样的现金流也是无法大批量及时地购买武汉所急需的物资的。为此我们的团队在摸索几天时间后做出决定，并在极短的时间内与美国大型NGO建立合作，争取捐助意向，帮助他们与疫区医院对接，确定援助物资，并帮助他们完成运输物资所需要的所有文件，协调运输通关，以及通过国内热心校友与志愿者们保驾护航，确保物资快速顺利到达指定医院。1月31日在武汉协和医院物资告急的时刻，终于将第一批Direct Relief捐赠的2.5吨医疗物资直接送达！详细报道请参考公众号前文，及全程录像"
          },
          {
            'source': {
                'title': "",
                'content': 'https://www.youtube.com/watch?v=6SqgCPgioVE',
                'link': 'https://www.youtube.com/watch?v=6SqgCPgioVE'
            }
          },
          {
            'paragraph': '除了与Direct Relief进行合作，我们也和MAP International建立了合作伙伴关系。我们承诺将部分捐款用于支持他们。由MAP International牵头，Wuhan United 以及其他捐赠机构共同捐助的超过134万个口罩，1万件防护服，还有28万双手套将发往湖北疫区。具体报道请参考'
          },
          {
            'source': {
                'title': "",
                'content': 'https://sites.google.com/view/wuhan-ncov-crisis-fundraise/our-work/wuhan-united-partnered-with-map-international',
                'link': 'https://sites.google.com/view/wuhan-ncov-crisis-fundraise/our-work/wuhan-united-partnered-with-map-international'
            },
          },
          {
            'source': {
                'title': "",
                'content': 'https://www.map.org/media',
                'link': 'https://www.map.org/media'
            },
          },
          {
            'paragraph': '今后短期内Wuhan United的工作重心将以这种模式继续与拥有稳定货源的大型NGO合作，促进更多的医疗资源迅速支援疫区。募集的资金一部分将用于深化与NGO的合作，以支持他们对疫区的贡献。疫区的情况每天都在变，我们的工作也会根据情况进行调整，一定尽我们所能为疫区做更多的事情。我们重申，所有募集到的资金都将用于支援疫区的工作中。谢谢大家的支持！'
          },
          {
            'sub_title': '重要更新声明'
          },
          {
            'paragraph': '基于目前通过武汉大学海外校友科学基金会善款捐赠的数额已经达到我们预先设定的范围，经Wuhan United执委会、武汉大学海外校友科学基金会和华科校友基金会商讨决定，武汉大学海外校友科学基金会将逐步停止受理对Wuhan United行动的捐赠，具体方式如下：'
          },
          {
            'list': [ '武汉大学海外校友基金会将会在美国西部时间2020年2月5日中午12时，停止代理接收针对Wuhan United的资金捐赠。同时，以免热心的朋友没有及时看到这一条消息，武汉大学海外校友基金会将把于美国西部时间2020年6月30日中午12时之前所有对武汉大学海外校友基金会的捐赠，用于支持Wuhan United，支持武汉，支持湖北，抗击新冠疫情。',
                      '华科校友基金会将继续为Wuhan United行动募集资金。',
                      '华科及武大北加州校友会的志愿者们将继续全力支持Wuhan United的后续支援行动'
                    ],
          },
          {
            'sub_title': 'Q&A'
          },
          {
            'paragraph': 'Q：目前已有哪些NGO合作对象'
          },
          {
            'paragraph': 'A：我们已经和Direct Relief和MAP International建立了合作关系。同时我们也在积极寻求更多NGO的合作机会。'
          },
          {
            'paragraph': 'Q：资金去向'
          },
          {
            'paragraph': 'A：已经募集的资金一部分将用于深化与NGO的合作，以支持他们对疫区的贡献。疫区的情况每天都在变，我们的工作也会根据情况进行调整，一定尽我们所能为疫区做更多的事情。我们重申，所有募集到的资金都将用于支援疫区的工作中。'
          },
          {
            'paragraph': 'Q：如何确保这些NGO的资金和物资能够用到中国疫情中'
          },
          {
            'paragraph': 'A：我们会以各种方式参与NGO的关于疫情捐赠事宜，从争取捐助意向，帮助他们与疫区医院对接，确定援助物资，帮助他们完成运输物资所需要的所有文件，协调运输通关，以及通过国内热心校友与志愿者们保驾护航，确保物资快速顺利到达指定医院。'
          },
          {
            'paragraph': 'Q：捐款平台会有手续费吗'
          },
          {
            'paragraph': 'A：”The GoFundMe platform is free. A standard transaction fee of 2.9% plus $0.30 per donation allows for credit card processing and safe transfer of funds.” (Quoted from Gofundme FAQ)； PayPal有募捐手续费每笔2.2%或2.9%+$0.30'
          },
          {
            'paragraph': 'Q：各个账户多久可以到账'
          },
          {
            'paragraph': 'A：Gofundme：“All donations are made directly to PayPal Giving Fund (a 501(c)(3) charitable organization). After the deduction of payment processing fees, PayPal Giving Fund delivers the funds they receive on a monthly basis. Payment processing fees including PayPal‘s transaction fee and GoFundMe’s processing cost for the secure transfer of funds. PayPal Giving Fund does not charge a fee for its services.” (Quote from Gofundme policies)； Benevity 账期至少为1个月'
          },
          { 
            'paragraph': 'Q：我们如何知道捐款情况的更新'
          },
          {
            'paragraph': 'A：每周会在网站和公众号上更新募捐情况与工作进展。'
          }
        ]
        # notice end

    ]
}

# information about contact。
contact_us_info = {

}

# information about qa pages
qa_info = {

}


# pass page info to correct page
menus2page = {
  'index': index_info,
  'alumni_activities': alumni_activities_info,
  'wuhan_situation': wuhan_situation_info,
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





























