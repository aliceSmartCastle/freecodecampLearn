from pprint import pprint


class EnglishDict:
    def __init__(self, translate_lang: str = "CN") -> None:
        self.word: list[str] = []
        self.translate: list[str] = []
        self.__translate_lang = translate_lang
        self.EN_CN: tuple[dict[str, str], ...] = ()

    def dict_append(self, *word_trans: dict[str, str]) -> None:
        self.EN_CN += word_trans
        for i in range(len(word_trans)):
            self.word.append(list(word_trans[i].keys())[0])
            self.translate.append(list(word_trans[i].values())[0])

    def dict_show(self) -> tuple[dict[str, str], ...]:
        return self.EN_CN

    def sort_dict(self, reverse: bool = False) -> tuple[dict[str, str], ...]:
        sort_temp = sorted(self.EN_CN, key=lambda x: list(x.keys())[0], reverse=reverse)
        return tuple(sort_temp)

    def trans_lang(self) -> None:
        if self.__translate_lang == "CN":
            print("translate to CN")
        else:
            print("not chosen the origin language to use")

    def word_count(self) -> str:
        return f"this dictionary recording difficult word amount is --> {len(self.EN_CN)}"


if __name__ == "__main__":
    test_word = EnglishDict()
    test_word.dict_append({"general": "通用"}, {"category": "类别"}, {"literal": "文字"}, {"interpolation": "插值"},
                          {"compact": "紧凑"}, {"increment": "递增"},
                          {"purpose": "目的"}, {"surpass": "超越"}, {"field": "领域"}, {"intelligent": "智能"},
                          {"concatenate": "连接"}, {"respective": "各自的"},
                          {"science": "科学"}, {"technology": "技术"}, {"artificial": "人工"}, {"individual": "个人"},
                          {"combine": "结合"}, {"omit": "省略"},
                          {"automation": "自动化"}, {"embedded": "嵌入式"}, {"library": "库"}, {"analysis": "分析"},
                          {"modify": "修改"}, {"alter": "变化"},
                          {"tedious": "繁琐"}, {"accessible": "易理解"}, {"available": "可用"}, {"immutable": "不可变"},
                          {"bracket": "括号 "}, {"notation": "符号"},
                          {"scalable": "可扩增的"}, {"platform": "平台"}, {"professional": "专业"}, {"absence": "缺席"},
                          {"primitive": "原始的"}, {"hood": "兜帽"},
                          {"cybersecurity": "网络安全"}, {"ethical": "伦理的"}, {"detect": "检测"}, {"against": "反对"},
                          {"negative": "负数"}, {"indicate": "指出"},{'orbit':"轨道"},{"simulator":"模拟器"},
                          )
    test_word.dict_append({"vulnerability": "漏洞"}, {"malware": "恶意软件"}, {"viruses": "病毒"}, {"exploit": "利用"},
                          {"curly-braces": "花括号"},{"rare":"稀有"},{"hardcode":"硬编码"},{"temporary":"临时"},
                          {"scans": "扫描"}, {"threat": "恐吓"}, {"dynamic": "动态"}, {"explicitly": "明确"},
                          {"contrast": "对比"}, {"prepares": "准备"}, {"triple": "三倍"},
                          {"compatibly": "兼容"}, {"monitor": "监督"}, {"strength": "实力"}, {"lead": "引导"},
                          {"determines": "确定"}, {"behave": "表现"}, {"treated": "对待"},
                          {"spreadsheet": "电子表格"}, {"extract": "取出"}, {"interact": "互动"}, {"algorithm": "算法"},
                          {"expect": "预料"}, {"sequence": "序列"},{"actual":"实际"},{"belong":"属于"},
                          {"scrape": "刮擦"}, {"property": "属性"}, {"parentheses": "圆括号"}, {"surround": "环绕"},
                          {"certain": "有把握"}, {"decimal": "小数"}, {"opposite": "迥异"},
                          {"deploy": "部署"}, {"large-scale": "大规模"}, {"through": "穿越"}, {"quotation": "引语"},
                          {"commas": "逗号"}, {"enclose": "包住"}, {"wrap": "包"},
                          {"industrial-level": "工业级"}, {"regardless": "不管"}, {"specialized": "专业化的"},
                          {"several": "一些"}, {"reveal": "透露"}, {"indentation": "缩进"},
                          {"security": "安全"}, {"hover": "悬停"}, {"modal": "模态"}, {"previous": "以前的"},
                          {"interpreter": "解释器"}, {"terminal": "终端"}, {"vice-verse": "反之亦然"}
                          , {"relies": "依赖"}, {"flavor": "风味"}, {"executable": "可执行的"}, {"declare": "声明"},
                          {"assign": "赋值"}, {"identifier": "标识符"}, {"reference": "论及"})
    test_word.dict_append({"series": "系列"}, {"character": "个性"}, {"represent": "作为"}, {"underscore": "下划线"},
                          {"alphanumeric": "字母数字"}, {"sensitive": "敏感的"}
                          , {"consider": "细想"}, {"reserved": "保留"}, {"syntax": "句法"}, {"convention": "惯例"},
                          {"separate": "分开"}, {"describe": "描述"}, {"communicate": "交流"}
                          , {"ignore": "忽视"}, {"multiple": "多个"}, {"consecutive": "连续的"}, {"reminder": "提醒"},
                          {"clarify": "澄清"}, {"instead": "相反"}, {"mentioned": "提及"}, {"prevent": "阻止"},
                          {"occurrent": "所有"}, {"prefix": "前缀 "}, {"suffix": "后缀"}, {"mathematical": "数学"},
                          {"arithmetic": "算术"}, {"calculate": "计算"}, {"perform": "进行"})
    test_word.dict_append({"addition": "加法"}, {"subtraction": "减法"}, {"division": "除法"}, {"modulo": "模除"},
                          {"exponentiation": "指数"}, {"multiplication": "乘法"},
                          {"asterisk": "星号"}, {"modular": "模数"}, {"efficient": "高效"}, {"concise": "简洁"},
                          {"redundancy": "冗余"}, {"potential": "潜在"}, {"arise": "出现"}, {"coion": "冒号"},
                          {"decrement": "递减"}, {"deliberate": "商榷"}, {"style": "风格"}, {"shortcuts": "捷径"},
                          {"obvious": "明显"}, {"unary": "一元"}, {"explicit": "明确"}, {"evaluate": "评价"},
                          {"constitute": "构成"}, {"placeholder": "占位符"}, {"determine": "决定"},
                          {"consistent": "持续的"}, {"clause": "条文"}, {"situation": "情况"}, {"extend": "延长"},
                          {"foundation": "基础"},
                          {"circuit": "环行"}, {"nested": "嵌套"}, {"eligible": "有资格"}, {"otherwise": "否则"},
                          {"refactor": "重构"}, {"discount": "折扣"}, {"entire": "全部的"}, {"invert": "倒置"}
                          , {"indicate": "表明"}, {"qualifies": "给与资格"}, {"membership": "会员资格"},
                          {"reusable": "可重复使用"}, {"referred": "参照"}, {"caesar-cipher": "凯撒密码"},
                          {"curriculum": "课程"}
                          , {"encrypt": "加密的"}, {"courage": "勇气"}, {"unlikely": "不太可能"}, {"decrypt": "解密"},
                          {"charisma": "魅力"}, {"octal": "八进制"}, {"hexadecimal": "十六进制"}, {"interval": "间隔"},
                          {"associate": "关联"}, {"particular": "特定"}, {"present": "展示"}, {"parallel": "平行线"},
                          {"comprehensive": "全面"}, {"aware": "察觉"}, {"fahrenheit": "华氏度"}, {"celsius": "摄氏度"},
                          {"confuse": "迷惑"}, {"practice": "练习"}, {"anonymous": "匿名"}, {"necessary": "必要"},
                          {"correspond": "对应"}, {"recipe": "食谱"}, {"alternation": "交替"}, {"brief": "简要"},
                          {"essential": "基本"}, {"technique": "技术"}, {"simultaneous": "同时"},
                          {"intersection": "交集"}, {"symmetric": "对称"}, {"vetted": "审查"}, {"abbreviate": "缩写"},
                          {"alias": "别名"},
                          {"conflict": "冲突"}, {"radian": "弧度"}, {"cosine": "余弦"}, {"discourage": "阻碍"},
                          {"collide": "碰撞"}, {"diagnosis": "诊断"}, {"hypertension": "高血压"},
                          {"diabetes": "糖尿病"},
                          {"asthma": "哮喘"}, {"chronic": "慢性"}, {"ensure": "确保"}, {"retrieve": "检索"},
                          {"resolve": "解決"}, {"involve": "涉及"}, {"utilize": "利用"}, {"contribute": "贡献"},
                          {"inspect": "检查"},
                          {"integrate": "整合"}, {"gutter": "沟"}, {"margin": "边"}, {"indicate": "表明"},
                          {"panel": "面板"}, {"pinpoint": "查明"}, {"examine": "检验"}, {"robust": "强壮的"},
                          {"fault-tolerant": "容错"},
                          {"anticipate": "预料"}, {"grace": "优雅"}, {"matter": "问题"}, {"recover": "恢复"},
                          {"enforce": "强制"}, {"insufficient": "不够"}, {"inherit": "继承"}, {"suppress": "压制"},
                          {"preserve": "保留"},
                          {"shorthand": "简写"}, {"strategic": "策略"}, {"feedback": "反馈"}
                          )
    print(test_word.word_count())

    pprint(test_word.sort_dict(), width=140, depth=90, compact=True, underscore_numbers=True)
