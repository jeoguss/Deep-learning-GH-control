# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:14:16 2018

@author: BICAL-JDH
"""
import numpy as np

B1 = np.array([2.0584607996301179,-1.602430904898126,1.5785971622662114,-1.8851910952625459,1.6978675521240907,0.97481827611609451,-1.2712659735145913,-0.96990523880988455,0.79434688845878887,-1.1785638435445873,-0.6639811853865043,0.10874365009695934,-0.27015214093984558,0.035482055126606744,-0.25849083876547047,-0.354743327448377,-0.35293763130855604,0.16478096885887586,0.85256557083725515,-0.6213154200728116,-0.38530305669288445,-0.83798411978830978,-1.1881311965432431,-0.88135715989790275,1.781967930692564,1.5034398216096438,1.1279252296025375,1.123966068137747,-1.3562654878051312,1.1886210607226131])

W1_1=np.array([[-0.499240677043898,1.12681186896910,0.483433601726229,2.34407825979180,-0.0564842868063009,-0.344370537458069,0.0129170029354844,-0.384445937506865,0.820997380970140,0.136234474077095,-0.322536668562151,0.0996985807221299,-0.444104158455878,0.548552968420485,-0.214394549882806],
              [0.316266481697971,0.0890955673961551,0.558218010654953,-0.255135979836301,0.454821955422111,-0.828786966814610,-0.286005219693294,-0.966667678215244,0.864798561586747,0.311425212952637,-0.509284948622118,-0.423419810424439,0.175144733460897,0.399499700793472,0.295639538791818],
              [0.230648259069952,0.0493915166878286,1.38438869813520,0.414669671327636,0.0135952177583910,0.994763782197302,0.296633191182517,-0.137661826669049,-0.117628965680076,-0.842812170980213,-0.167626974203837,0.00176885307575469,0.474674784289289,-1.07283137919078,0.453451718273171],
              [0.609326663760591,0.311772661723091,0.178474050444471,-1.60765009662242,0.00294528711695381,-0.656673456113445,1.09184762199322,-0.749256797826939,-0.465832895846085,0.0954423405570114,-0.275800430042787,0.734774428399677,0.660548884377460,0.396551454034686,0.121444222655458],
              [-1.11161134150532,-0.112780192545115,-0.343937716879292,0.406948199086829,0.0176647222771543,0.768521339631365,0.564839889099100,1.24531495051684,1.53029649532145,-0.448832773662287,0.0601810698976264,0.308642994699493,-0.835892353568136,-0.168173566949440,-0.00713050647369541],
              [-0.168741386933479,0.568749852687018,-0.585694114380041,-0.131828211269798,-0.0471564998852885,-0.750189554170740,0.705734664802713,0.674042442053103,1.69441687283198,-0.233878801168494,-0.211071380359505,0.529691685869981,0.365280146936690,0.114672395667469,0.861090667975291],
              [0.147406029669886,0.893943185010003,-1.46427340014174,-0.235999888723038,0.188446653755375,0.261995119303653,0.635820371434170,-0.632986879030688,-0.00639448922466440,-0.234908635959045,1.21568478784143,0.0430458021000523,0.330106672460335,-0.537670862377783,0.462972288209248],
              [0.369245527325807,0.690569812551087,-0.640663665870489,-0.399255146032392,0.167697911745227,0.0977041769747756,-0.0425806377519687,0.316882849469936,-0.174567855024121,-0.124522141018574,0.970609725171123,0.725472335462384,-0.0623081509770846,0.0116442155892254,0.788512525671015],
              [0.00571673378746296,1.01554492651119,-0.828685707085502,-0.184571754694711,-0.0492050827479366,-1.09077146974060,0.768784510761551,0.224763418450796,1.95093777110656,0.0852698972562340,-0.257796630859219,0.388141533234376,-0.237524028630839,0.0269124975019372,0.418657150809528],
              [1.20851482341047,-0.177431137311407,-0.0138543647331282,0.129964594201673,0.0768194051693655,-0.263997916032774,-0.286410432767026,-1.10462250309348,1.01585530524701,-0.665921250047046,-0.356672169372645,-0.124894990617372,0.253850919590712,0.244473327581680,0.835168186326373],
              [-0.0610589300474627,0.165886527313262,0.314399402987658,-1.06907898767122,-0.166146592152398,-0.210649637145594,0.178973383379588,-0.793764036890421,-0.999034387422320,0.774138352554396,0.480773978543800,0.255496017767713,-0.150036448142054,0.225722802316624,-0.309279923067200],
              [0.0821885634995946,-0.143467446497187,0.736651774411691,-1.01314410726232,-0.289258060422775,-0.0265296967503294,0.936409619968668,-0.872559608678696,-0.198379503318662,0.374409154316688,-0.416685949101623,-0.399107329639868,-0.122672291598166,-0.318542741321437,0.153322071277008],
              [0.301136892046642,-0.449396107676850,0.780330832464807,-0.521280424700137,-0.336480781723180,0.910418391365916,0.123386696758647,-0.520897459926971,-0.688565480944125,-0.0496682469250924,0.343726985369224,0.213417063033263,-0.593696667649748,-1.25790138311678,-0.155939104111007],
              [-1.25384347892344,-0.399267484555855,-0.120947524521545,0.804393122982822,0.0597491876489612,-0.0349077527519862,0.269935862495450,-0.235739347180317,0.552475961838505,-0.192961041419800,-0.350604332082471,-0.579980783513271,0.124468955617285,0.0565924186877360,-0.428698139355894],
              [-0.0233379956769271,0.870972850637093,-1.11983182483065,0.409163490872813,0.0627690206572851,-1.62567398810232,-0.246650893695629,-0.820104627789288,-1.79093083791786,0.391229237481683,-0.764269931061963,0.570132057152175,-0.191878752214581,-0.0706929656630416,-0.467613548076158],
              [-0.0825798745935233,-0.623152702810977,-0.188485157175923,0.964380307557033,0.101753155472978,0.338320537979526,-0.648162386354734,0.502229761280216,-0.763097989716086,0.0755417523899369,0.187319048775955,-0.331803880655079,-0.0543849046288637,-0.00431171791488491,0.599035608992936],
              [0.628989040161583,-0.859658763509123,-0.446062279801237,-2.76975366180789,-0.00130359179264390,0.366441456683889,0.827441607208757,0.224161476047414,-1.34272155498349,-0.230198845022042,-0.0149331335856326,0.873380044880796,0.644221208292081,-0.109405353542378,0.848015472304623],
              [0.0683869730380426,-0.532519942216769,-0.752896563489743,0.289274287968010,0.138055539924999,-0.0455203502357018,-0.523077435143042,-0.160804315186069,-1.93455279667202,-0.611286097115644,0.452649818629931,0.755231007908528,0.227375516097644,0.663481843119260,-0.468179392677831],
              [1.07248383186991,-0.257565197913024,-0.608578277563776,0.690543258730675,-0.164045068292595,1.12243395371372,-0.0652120100428599,-0.838389816890895,0.800126118906263,-1.17359008516740,-0.770037857546045,-0.0723753627475751,-0.535102149456964,0.0296798003277561,-0.467832080549080],
              [-0.732450503887755,-1.13748990243899,-0.183945344402317,0.0373764169313657,0.435090486396837,0.969366487779226,-0.0526841164107505,0.358176862984193,0.614341747860470,-1.30402099148103,0.288896587116497,-0.0156739924163289,-0.0775628094461958,-0.641830365051223,0.892194714696639],
              [-1.98888434133396,-0.353372654771364,-0.275729978534295,1.09060403845604,-0.0389683985220313,-0.923058289294690,-0.854333367087028,0.215455793250102,0.633872379721778,-0.0343565083811334,-0.330958287322337,-0.00461128523565300,-0.176289791262049,-0.547856075279834,-0.902510711959921],
              [-1.62288756849802,-0.127200068233586,0.156513035690315,1.40917248788776,0.377826885132925,1.12490577674369,0.635984678452225,0.0518083485332889,0.149875427053670,-0.581978339640193,-0.293879474246725,0.473099111151808,-2.07191982430298,-0.322953024916743,0.193061046732988],
              [-2.29324441156281,-1.03125823117112,0.0923140316672409,-1.73552524662737,0.144936039934695,0.143262402102089,-0.148840746859412,1.27199976547261,0.313661107329280,0.616532594937864,0.337324867227210,0.00128842880002952,1.29574887504864,0.860261179115574,0.0991272658930095],
              [0.773129722486506,0.0532179273723280,-0.716913618589047,-0.145280658099374,0.0594190991437833,0.548524237498900,0.248595141176382,-0.695420702874948,1.01650361056111,-0.605226642152608,-0.200762163914119,0.818252405908065,0.331669452981103,0.0920269332623436,-0.323888523107162],
              [3.09044357317946,0.875391690711471,0.0915089744178327,2.49206991956554,-0.199909613254744,-0.391396974448028,-0.407984932289072,0.0612756078971773	,-0.149269179465401,1.14540622857044,0.501519852884621,-1.28787023214376,-0.607763202864061,-0.801755915797146,-0.741017113149505],
              [1.87111084441077,-0.150277548562405,0.286970790306249,-0.292490621660181,0.0119950164660650,0.232461088409779,-0.991689675483200,-0.334063754056580,-1.11453402419352,-0.144630057904108,0.425233811475337,0.149752925989434,0.713970042379288,0.964773798343115,0.567390021321354],
              [0.367772919771707,-1.78668798430347,0.158784346911764,0.311557968498614,0.135038228366107,-0.348334054095726,0.348410807770512,-0.854905179459514,-1.14853105200863,0.346867167010402,0.212864880242209,-0.507687416726631,-0.667698613005815,-0.149961657779768,0.371752639854012],
              [0.378793490078708,-1.70099726752056,1.52292657671124,-1.45977534643208,-0.136262548903844,-0.0336236226136569,-0.216481121165499,0.184634582157213,-0.306419533458077,1.49833552806503,0.415804885870890,0.438797274190197,-0.595983416729210,-0.744036747662182,0.627910661989356],
              [0.931005093889287,-0.00860970763421289,0.821698949984528	,-0.134612774975464,0.533511628918645,0.161897591982430,-0.445279520763715,-1.41908477051362,1.30506076207449,-1.18532258481125,-0.187288993232417,-0.0317425880245653,0.218949059771547,1.31159807939363,-0.678289418072134],
              [-0.822961696810312,-0.110888168896404,-0.0982526698771855,-1.80115452608442,-0.212636752480956,0.0267073275005324,-0.0399011711258060,0.356410798373880,-0.0847038333640180,-0.220621570704176,-0.196097080770979,-0.355403844450059,-0.751706997464698,0.994892152759545,0.130199539257727]])




# Layer 2 #
B2 =-0.36047256216576545
W2_2=np.array([-0.52085555431743769,-0.42064221809714769,-0.26656468021690366,0.86291449824433197,-0.33395727095299305,-1.1303178785486472,-0.28649617297232982,-0.57677702580228152,0.92656703550288477,-1.2744107133313769,-0.28561228790265147,-0.76083109533272653,0.30594012834717854,0.71281662464683526,-0.17482328798626071,-0.90831677613014195,-0.69696926202477671,-0.51941124945497086,-0.26459403135654497,-0.24722743824884477,-0.28633840339075289,0.30179894916436689,-0.097092480594107716,1.8201827247352609,0.20081602777261129,0.43389342926447877,-0.55948688113494127,0.12412569763216194,0.26730889199075458,-0.46626489873288285])
# regulization  #
Xr_Xoffset=([0.000694444,0.4,17,0,0,301,11.8,17.9,-26.099999,0,0,0,0,0,0])
Xr_Xgain=([2.0040633486629,0.051150895140665,0.027027027027027,0.0015625,0.222222222222222,0.00550964187327824,0.00394321766561514,0.0257731958762887,0.0345423149316462,2,2,0.000621890547263682,2,2,0.0000772946859903382])
Xr_Xmin=-1
# Output1#
Y_Ymin=-1
Y_YGain=0.072992700729927
Y_Yoffset=11.8
