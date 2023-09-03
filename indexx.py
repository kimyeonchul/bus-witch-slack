import boto3

# AWS 자격 증명 설정
aws_access_key_id = 'AKIAZFEQRMP3YZLAEKJU'
aws_secret_access_key = '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'
region_name = 'ap-northeast-2'

# QuickSight 클라이언트 생성
quicksight = boto3.client('quicksight', 
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

# # QuickSight 대시보드 ID
# dashboard_id = 'bd9fc5ca-5114-4445-bf27-a33d0eeb78a4'

# # 대시보드 데이터 가져오기
# response = quicksight.get_dashboard(
#     # AwsAccountId='629515838455',
#     # DashboardId=dashboard_id
#         DashboardName='메인대쉬보드'

# )

dashboard_arn = 'arn:aws:quicksight:ap-northeast-2:629515838455:dashboard/bd9fc5ca-5114-4445-bf27-a33d0eeb78a4'

# 대시보드 가져오기
# response = quicksight.describe_dashboard(
#     AwsAccountId='629515838455',  # AWS 계정 ID
#     DashboardId=dashboard_arn
# )

# # 가져온 대시보드 출력
# print(response)

# # 대시보드 데이터 출력
# print(response)


# QuickSight 대시보드 목록 가져오기
# response = quicksight.list_dashboards(
#      AwsAccountId='629515838455',
#    MaxResults=10  # 최대 결과 수 (원하는 값으로 설정)
# )

# 대시보드 목록 출력
# print(response['DashboardSummaryList'])


# 대시보드를 임베드하고 URL 생성
response = quicksight.get_dashboard_embed_url(
    AwsAccountId='629515838455',  # AWS 계정 ID
    DashboardId='bd9fc5ca-5114-4445-bf27-a33d0eeb78a4',  # 대시보드 ID 또는 ARN
    IdentityType='IAM',  # 인증 유형 (IAM 사용)
    ResetDisabled=True  # 대시보드 임베드 시 임베드된 사용자의 상태 초기화 여부
)

# 생성된 URL 출력
print(response['EmbedUrl'])
