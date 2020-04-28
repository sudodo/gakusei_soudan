import pandas as pd

def make_file_with_sensei_name(sensei_name):
	"""先生の名前を入れると、先生のpandasが生成されます。"""
	return None

necessary_columns = ["学籍番号", "氏名" .....]
input_df = pd.read_excel("../機密ファイル.xlsx")
output_df = input_df.loc[:, necessary_columns]
output_df["評価"] = ""
output_df["詳細報告_コメント"] = ""

sensei_name_list = set(input_df["指導教員"])
for sensei_name in sensei_name_list:
	sensei_gotono_df = make_file_with_sensei_name(sensei_name)
	pd.to_excel("相談週間_"+sensei_name)
