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

    ```
    {
        "Name":[String],  // メンバー名配列（必須）
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
                "GroupMember":[String]  // メンバー名リスト
            }
        ]
    }
    ```

- Ex-1
    - Request
        ```
        {
            "Name":["A","B","C","D","E","F","G"],
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
                    "GroupMember":["C","D","F","G"],
                },
                {
                    "GroupName": "Group-2",
                    "GroupMember":["A","B","E"]
                }
            ]
        }
        ```

- Ex-2
    - Request
        ```
        {
            "Name":["A","B","C","D","E","F","G"],
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
                    "GroupMember":["C","D","F"]
                },
                {
                    "GroupName": "Group-2",
                    "GroupMember":["A","B","E"]
                },
                {
                    "GroupName": "MuraHachibu",
                    "GroupMember":["G"]
                }
            ]
        }
        ```