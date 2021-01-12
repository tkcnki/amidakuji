# amidakuji
３人または４人のグループ分けを行うLINEボット

## 要件
- ~~LINE~~ Slackボットとして動作する
- メンバーをグループに分ける
- １グループは４人または３人
- メンバーの最小は３人
- メンバーが５人以外の場合、余りは０
- グループの人数を固定にすることも可能（１０人を４，４，余り２に分ける）

## API

memo: レスポンスはSlackの戻り形式に合わせる必要あり。

### [GET] /amida
- Request  

    ```
    {
        "Names":[String],  // メンバー名配列（必須）
        "NumberInGroup":int  // １グループの人数を固定にする場合指定（任意）
    }
    ```

- Response  
    Status Code: 200  
    ```
    {
        "Groups":
        [
            {
                "GroupName": String,    // グループ名
                "GroupMembers":[String]  // メンバー名リスト
            }
        ]
    }
    ```

- Ex-1
    - Request
        ```
        {
            "Names":["A","B","C","D","E","F","G"],
            "NumberInGroup":0
        }
        ```

    - Response  
        Status Code : 200
        ```
        {
            "Groups":
            [
                {
                    "GroupName": "Group-1",
                    "GroupMembers":["C","D","F","G"],
                },
                {
                    "GroupName": "Group-2",
                    "GroupMembers":["A","B","E"]
                }
            ]
        }
        ```

- Ex-2
    - Request
        ```
        {
            "Names":["A","B","C","D","E","F","G"],
            "NumberInGroup":3
        }
        ```

    - Response  
        Status Code : 200
        ```
        {
            "Groups":
            [
                {
                    "GroupName": "Group-1",
                    "GroupMembers":["C","D","F"]
                },
                {
                    "GroupName": "Group-2",
                    "GroupMembers":["A","B","E"]
                },
                {
                    "GroupName": "MuraHachibu",
                    "GroupMembers":["G"]
                }
            ]
        }
        ```