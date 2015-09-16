acitoolkit을 활용하며 특정 테넌트 생성하는 script 입니다.

EPG와 BD를 1대1 매핑하고 BD에 설정된 gateway/subnet을 구성하는 예제로 mydata.csv 파일을 구성하시면 됩니다.
MyTenant 부분에 사용하실 Tenant이름을 적어주시고 
MyApp 부분에 사용하실 Application Profile을 적고
MyNetwork 부분에 private network 이름을 적어주시면 됩니다.


기본적으로 acitoolkit을 설치되어야 하며 설치를 위해서는 github.com/datacenter/acitoolkit 에서 확인하세요 
APIC 정보는 credentials.py 를 수정하셔서 id, password, http or https를 설정하세요 

python build_tenant_with_csv.py 만 입력하시면 mydata.csv 내용일 읽어서 처리하게 tenant를 생성하게 됩니다. 
