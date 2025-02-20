import os
import re


# 获取 ERPNext 版本
def get_erpnext_version():
    erpnext_version = os.getenv("ERPNEXT_VERSION")
    assert erpnext_version, "No ERPNext version set"
    return erpnext_version


# 更新环境配置文件
def update_env(erpnext_version: str):
    with open("example.env", "r+") as f:
        content = f.read()
        content = re.sub(
            rf"ERPNEXT_VERSION=.*", f"ERPNEXT_VERSION={erpnext_version}", content
        )
        f.seek(0)
        f.truncate()
        f.write(content)


# 主函数
def main() -> int:
    update_env(get_erpnext_version())
    return 0


# 程序入口
if __name__ == "__main__":
    raise SystemExit(main())