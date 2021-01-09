# amidakuji
３人または４人のグループ分けを行うLINEボット

## 要件
- LINEボットとして動作する
- メンバーをグループに分ける
- １グループは４人または３人
- メンバーの最小は３人
- メンバーが５人以外の場合、余りは０
- グループの人数を固定にすることも可能（１０人を４，４，余り２に分ける）

## API
### [GET] /amida
- Request
    ---JSON
    {
        "Name":[String],  // メンバー名配列（必須）
        "NumberInGroup":int  // １グループの人数を固定にする場合指定（任意）
    }
    ---

- Response
    Status Code: 200     
    ---JSON
        {
            "Groups":
            [
                {
                    "GroupName": String,    // グループ名
                    "GroupMember":[String]  // メンバー名リスト
                }
            ]
        }
    ---
