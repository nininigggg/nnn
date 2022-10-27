import time

import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.drvier = webdriver.Chrome()

    def test_get_cookies(self):
        # 1. 访问企业微信主页/登录页面
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 2. 等待20s，人工扫码操作
        time.sleep(20)
        # 3. 等成功登陆之后，再去获取cookie信息
        cookie = self.drvier.get_cookies()
        # 4. 将cookie存入一个可持久存储的地方，文件
        # 打开文件的时候添加写入权限
        with open("cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)

    def test_add_cookie(self):
        # 1. 访问企业微信主页面
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.drvier.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")


"""
yaml相关依赖
"""

# <properties>
#   <!--对应解析-->
#   <jackson.version>2.13.1</jackson.version>
# </properties>
#
# <dependencies>
#   <!--        yaml文件解析-->
#   <dependency>
#       <groupId>com.fasterxml.jackson.core</groupId>
#       <artifactId>jackson-databind</artifactId>
#       <version>${jackson.version}</version>
#   </dependency>
#   <dependency>
#       <groupId>com.fasterxml.jackson.dataformat</groupId>
#       <artifactId>jackson-dataformat-yaml</artifactId>
#       <version>${jackson.version}</version>
#   </dependency>
# </dependencies>


"""
Java代码
"""
# package com.ceshiren.hogwarts;
# import com.fasterxml.jackson.core.type.TypeReference;
# import com.fasterxml.jackson.databind.ObjectMapper;
# import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
# import org.junit.jupiter.api.AfterAll;
# import org.junit.jupiter.api.BeforeAll;
# import org.junit.jupiter.api.Test;
# import org.openqa.selenium.Cookie;
# import org.openqa.selenium.chrome.ChromeDriver;
# import org.openqa.selenium.support.ui.WebDriverWait;
# import java.io.File;
# import java.io.IOException;
# import java.time.Duration;
# import java.util.HashMap;
# import java.util.List;
# import java.util.Set;
#
# public class CookieTest {
#
#     private static ChromeDriver driver;
#     private static WebDriverWait wait;
#     final ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
#
#     @BeforeAll
#     public static void beforeAll() {
#         driver = new ChromeDriver();
#         driver.get("https://work.weixin.qq.com/wework_admin/frame");
#         wait = new WebDriverWait(driver, Duration.ofSeconds(1000));
#     }
#     @AfterAll
#     public static void afterAll() throws InterruptedException {
#         Thread.sleep(10000);
#         driver.quit();
#     }
#     // Cookie读取的步骤
#     @Test
#     public void saveCookies() throws IOException {
#         // 1. 获取当前的url
#         String url = driver.getCurrentUrl();
#         // 2. 扫码跳转页面
#         // 3. 显式等待判断当前的url不等于前面获取的url
#         wait.until(webDriver -> !webDriver.getCurrentUrl().equals(url));
#         // 4. 登录成功后获取当前的cookie信息
#         Set<Cookie> cookies = driver.manage().getCookies();
#         // 5. 写入cookie
#         mapper.writeValue(new File("cookies.yaml"), cookies);
#     }
#     // Cookie写入的步骤
#     @Test
#     public void loadCookies() throws IOException {
#         // 1.声明一个泛型
#         TypeReference<List<HashMap<String, Object>>> typeReference =
#                 new TypeReference<>() {};
#         // 2. 从yaml中获取cookies
#         List<HashMap<String, Object>> cookies =
#                 mapper.readValue(new File("cookies.yaml"),
#                         typeReference);
#         cookies.stream()
#         // 找到domain包含work.weixin.qq.com
#         .filter(cookie -> cookie.get("domain").toString().
#                 contains("work.weixin.qq.com"))
#         .forEach(cookie -> {
#             driver.manage().addCookie(
#                 new Cookie(cookie.get("name").toString(),
#                         cookie.get("value").toString()));
#         });
#         // 4. 刷新页面，登录成功
#         driver.navigate().refresh();
#     }
# }