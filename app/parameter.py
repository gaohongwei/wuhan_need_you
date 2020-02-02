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

    'home_images': ["image/alumni_activities/2018_bbq.jpg", "image/alumni_activities/2017_president.jpg", "image/wuhan_situation/h1.jpg", "image/wuhan_situation/h6.jpg"],

    'alumni_association': {
      'title': "武汉大学北加州校友会",
      'content': "武汉大学北加州校友于1980s成立于加州硅谷，是武汉大学校友总会认可的合法合规海外校友会分支，是基金会的执行机构",
      'member_info': {
          'title': "校友会会长:",
          'member': ["巨辉 (现任会长)", "Harry Wang (副会长)", "沈睿 (副会长)", "陶然 (副会长)", "李晨晨 (副会长)"],
      },
      'legality': {
          'title': "机构资质认定",
          'link': "https://alumni.whu.edu.cn/gdxyh.htm"
      }
    },

    'foundation': {
      'title': "武汉大学海外校友科学基金会",
      'content': "由黄彰任、王高峰、李晓景三位武汉大学校友倡议, 基金会成立于1999年，A California Nonprofit Public Benefit Corporation，Public Charity, Under section 501(c)(3) a non-profit public benefit organization exempt from federal income tax under section 501(c)(3) of the Internal Revenue Code in USA.",
      'member_info': {
          'title': "基金会历任会长:",
          'member': ["黄彰任（名誉会长)", "李晓景（首任会长)", "宁挺", "王常玉", "欧阳明", "陈小春", "李金辉 (现任会长)"],
      }
    },

    'special_topic': {
      'title': "武汉加油行动专题",
      'image': "image/jiayou.jpeg",
      'link': 'wuhan_situation',
    }

}

# information about index pages
alumni_activities_info = {
  'home_images': ["image/alumni_activities/2019_life_science_1.jpg", "image/alumni_activities/2019_life_science_2.jpg", "image/alumni_activities/2019_3551.jpg", "image/alumni_activities/2018_university_council.jpg"],

  'activites_info': [
    {
      'title': "2019年10月 校友会年度BBQ (拔河掠影)",
      'image': ["image/alumni_activities/2019_life_science_1.jpg", "image/alumni_activities/2019_life_science_2.jpg"]
    }, 
    {
      'title': "2019年10月 校友会协办3551国际创业大赛(硅谷赛区)",
      'image': "image/alumni_activities/2019_3551.jpg"
    }, 
    {
      'title': "2019年8月校友会对接生命科学院暑期访学团",
      'image': ""
    }, 
    {
      'title': "2018年12 武大校友同武大院士教授欢聚",
      'image': ""
    }, 
    {
      'title': "2018年10月 校友会年度BBQ合影",
      'image': ""
    }, 
    {
      'title': "2018年10月校友会协办3551国际创业大赛(硅谷赛区)",
      'image': ""
    }, 
    {
      'title': "2018年8月校友会对接生命科学院暑期访学团",
      'image': ""
    }, 
    {
      'title': "2018年8月校友会代表队参与第16届北加州华人文化体育协会运动大会",
      'image': ""
    }, 
    {
      'title': "2018年4月 武大校董喻鹏和新一届校友会成员一起",
      'image': ""
    }, 
    {
      'title': "2017年 窦贤康校长与校友会在斯坦福组织武大海外恳谈会",
      'image': ""
    }, 
    {
      'title': "2017年武大校友会全体人员",
      'image': ""
    }, 
    {
      'title': "2017年校友会年度BBD(联合兄弟校友会和湖北同乡会)",
      'image': ""
    }, 
    {
      'title': "2015年11月 武汉大学副校长黄泰岩 在湾区招才引智",
      'image': ""
    }, 
    {
      'title': "2010年 武大校长刘经南到湾区看望武大校友",
      'image': ""
    }, 
    {
      'title': "2007年12月 黄彰任会长（前排居中），基金会成员与彭旧金山总领事合影",
      'image': ""
    }, 
    {
      'title': "2007年时任武汉市委书记（现任工信部部长）苗圩-左三与基金会部分成员（欧阳明-右二，王高峰-右一）合影",
      'image': ""
    }, 
    {
      'title': "2007年 刘经南 校长访问基金会留影",
      'image': ""
    }, 
    {
      'title': "2006年 校友会校友年度BBQ",
      'image': ""
    }, 
    {
      'title': "2005年宁挺，欧阳明，王高峰等代表基金会参与华人运动会",
      'image': ""
    }, 
    {
      'title': "1998年校友会成立大会合影留念",
      'image': ""
    }

  ]

}

# information about wuhan situation pages
wuhan_situation_info = {
  
}

# information about alumni action pages
alumni_action_info = {

}

# information about donate pages
donate_info = {
  
}

# information about contact us pages
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
  {
    "title": "第二批物资已于美国时间1月28日凌晨从纽约起飞......",
    "content": "第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......第二批物资已于美国时间1月28日凌晨从纽约起飞......",
    "source": "武大校友会",
    "date": '2020',
    "type": '捐赠',
    "tag": '物资',
    "status": 'active'
  },
  {
    "title": "第一批物资已于美国时间1月27日凌晨从纽约起飞......",
    "content": "第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......第一批物资已于美国时间1月27日凌晨从纽约起飞......",
    "source": "武大校友会",
    "date": '2020',
    "type": '捐赠',
    "tag": '物资',
    "status": 'active'
  },
]





























