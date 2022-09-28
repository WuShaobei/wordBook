from enum import Enum

class Types( Enum ) :
    err = "-99"
    notFindMsg = "The Word %s Was not Found."

    # 新增功能 
    append = "1"
    appenddMsg = "Append"

    # 查询功能
    select = "2"
    selectMsg = "Select"

    # 更新功能
    update = "3"
    updateMsg = "Update"

    # 删除功能
    delete = "4"
    deleteMsg = "Delete"

