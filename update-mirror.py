from xml.dom import minidom

import sys
import os
import platform
import tempfile
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement

def print_diff(s1: str, s2: str):
    import difflib
    for line in difflib.unified_diff(s1.splitlines(), s2.splitlines()):
        print(line)

def xml_to_str(root):
    reparsed = minidom.parseString(ET.tostring(root))
    return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])

def process_java_maven():
    maven_conf_path = os.getenv("HOME") + "/.m2/settings.xml"
    assert os.path.exists(maven_conf_path), f"Maven 配置文件 {maven_conf_path} 不存在"
    tree = ET.parse(maven_conf_path)
    root = tree.getroot()
    existing_mirrors = {}
    for mirror_node in root:
        id_ = mirror_node.find("id").text
        name = mirror_node.find("name").text
        url = mirror_node.find("url").text
        mirrorOf = mirror_node.find("mirrorOf").text
        if "maven.aliyun.com" in url:
            print("检测到可能过时的 maven.aliyun.com 配置")
            root.remove(mirror_node)
        else:
            existing_mirrors[url] = {
                "id": id_,
                "name": name,
                "mirrorOf": mirrorOf
            }
    # https://maven.aliyun.com/mvn/guide
    if "https://maven.aliyun.com/repository/public" not in existing_mirrors:
        mirror_node = SubElement(root, 'mirror')
        id_node = SubElement(mirror_node, "id")
        id_node.text = "aliyunmaven"
        name_node = SubElement(mirror_node, "name")
        name_node.text = "阿里云公共仓库"
        url_node = SubElement(mirror_node, "url")
        url_node.text = "https://maven.aliyun.com/repository/public"
        mirrorOf_node = SubElement(mirror_node, "mirrorOf")
        mirrorOf_node.text = "*"

    print(f"========== 是否按如下 diff 更新 {maven_conf_path}? ==========")
    print_diff(xml_to_str(ET.parse(maven_conf_path).getroot()), xml_to_str(root))
    input(f"========== 按 Enter 更新 {maven_conf_path}, Ctrl-C 取消 ==========\n")
    tmp_name = tempfile.NamedTemporaryFile(delete=False).name
    os.rename(maven_conf_path, tmp_name)
    with open(maven_conf_path, "w") as fh:
        fh.write(xml_to_str(root))
    print(f"========== {maven_conf_path} 已更新，原文件已备份至 {tmp_name} ==========")

if __name__ == "__main__":
    lang = sys.argv[1]
    repo_type = sys.argv[2]

    current_system = platform.system()
    assert current_system in ["Darwin"], f"暂不支持 {current_system}"

    if current_system == "Darwin":
        if lang == "java":
            if repo_type == "maven":
                process_java_maven()
                exit(0)

    print(f"暂时不支持的参数: {lang} {repo_type}，请提 issue 给我们")