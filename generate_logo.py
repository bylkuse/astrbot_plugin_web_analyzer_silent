#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成网页分析插件logo的脚本
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    # 创建256x256像素的图像
    size = (256, 256)
    img = Image.new('RGBA', size, (255, 255, 255, 0))  # 透明背景
    draw = ImageDraw.Draw(img)
    
    # 设计logo元素
    # 1. 创建现代渐变背景效果 - 使用深色到浅色的径向渐变
    center = (128, 128)
    radius = 128
    
    # 绘制渐变圆形背景
    for r in range(radius, 0, -1):
        # 从深蓝到浅蓝的渐变
        alpha = int(255 * (r / radius))
        color = (30, 64, 175, alpha)  # 深蓝色
        draw.ellipse([center[0]-r, center[1]-r, 
                      center[0]+r, center[1]+r], 
                     fill=color)
    
    # 2. 添加网页分析主图标
    # 中心六边形作为底座
    hexagon_points = []
    hex_radius = 80
    for i in range(6):
        angle = (i * 60) * 3.14159 / 180
        x = center[0] + hex_radius * 0.7 * (1 if i % 2 == 0 else 0.87) * (1 if i < 3 else -1)
        y = center[1] + hex_radius * 0.5 * (1 if i < 3 else -1)
        hexagon_points.append((x, y))
    draw.polygon(hexagon_points, fill=(255, 255, 255, 220), outline=(255, 255, 255, 255), width=2)
    
    # 3. 添加浏览器窗口图标
    browser_width = 100
    browser_height = 70
    browser_x = center[0] - browser_width//2
    browser_y = center[1] - browser_height//2
    
    # 浏览器主体
    draw.rectangle([browser_x, browser_y, 
                    browser_x + browser_width, browser_y + browser_height], 
                   fill=(30, 64, 175, 255), outline=(255, 255, 255, 255), width=2)
    
    # 浏览器地址栏
    address_bar_height = 12
    draw.rectangle([browser_x + 5, browser_y + 5, 
                    browser_x + browser_width - 5, browser_y + 5 + address_bar_height], 
                   fill=(255, 255, 255, 200), outline=(200, 200, 200, 200), width=1)
    
    # 浏览器标签页
    tab_width = 30
    tab_height = 10
    draw.rectangle([browser_x + 10, browser_y - tab_height, 
                    browser_x + 10 + tab_width, browser_y], 
                   fill=(30, 64, 175, 255), outline=(255, 255, 255, 255), width=2)
    
    # 4. 添加分析图标（升级版放大镜）
    magnifier_center = (center[0] + 35, center[1] + 25)
    magnifier_radius = 20
    handle_length = 25
    
    # 放大镜镜片（渐变效果）
    for r in range(magnifier_radius, 0, -1):
        alpha = int(255 * (r / magnifier_radius))
        draw.ellipse([magnifier_center[0]-r, magnifier_center[1]-r,
                      magnifier_center[0]+r, magnifier_center[1]+r],
                     fill=(30, 64, 175, alpha), outline=(255, 255, 255, 255), width=2)
    
    # 放大镜手柄
    handle_end_x = magnifier_center[0] + magnifier_radius + handle_length
    handle_end_y = magnifier_center[1] + magnifier_radius + handle_length
    draw.line([magnifier_center[0] + magnifier_radius, magnifier_center[1] + magnifier_radius,
               handle_end_x, handle_end_y], 
              fill=(255, 255, 255, 255), width=3)
    
    # 5. 添加数据分析线条
    # 三条动态线条代表数据流动
    for i in range(3):
        start_x = browser_x + 15 + i * 25
        start_y = browser_y + browser_height + 5
        end_x = start_x + 10
        end_y = start_y + 20
        
        # 连接线
        draw.line([start_x, start_y, end_x, end_y], 
                  fill=(255, 215, 0, 255), width=2)
        
        # 连接点（动态效果）
        dot_radius = 4
        draw.ellipse([end_x-dot_radius, end_y-dot_radius, end_x+dot_radius, end_y+dot_radius], 
                     fill=(255, 215, 0, 255), outline=(255, 255, 255, 255), width=1)
    
    # 6. 添加文字标识
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("arial.ttf", 22)
        text = "WebAnalyzer"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        text_x = center[0] - text_width // 2
        text_y = center[1] + radius - 40

        draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    except Exception as e:
        # 如果字体不可用，尝试其他系统字体
        try:
            font = ImageFont.truetype("Microsoft YaHei UI", 18)
            text = "WebAnalyzer"
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            text_x = center[0] - text_width // 2
            text_y = center[1] + radius - 40

            draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
        except Exception:
            # 如果所有字体都不可用，跳过文字
            pass
    
    # 7. 添加装饰性圆环
    outer_ring_radius = 120
    draw.ellipse([center[0]-outer_ring_radius, center[1]-outer_ring_radius, 
                  center[0]+outer_ring_radius, center[1]+outer_ring_radius], 
                 outline=(255, 255, 255, 150), width=1)
    
    return img

def main():
    print("正在生成网页分析插件logo...")
    
    # 创建logo
    logo = create_logo()
    
    # 保存为PNG文件
    output_path = os.path.join(os.path.dirname(__file__), "logo.png")
    logo.save(output_path, "PNG")
    
    print(f"Logo已成功生成并保存到: {output_path}")
    print("Logo尺寸: 256x256 像素")
    print("Logo格式: PNG (透明背景)")
    
    # 显示logo信息
    print("\nLogo设计说明:")
    print("- 深蓝色渐变圆形背景代表网络和科技")
    print("- 六边形底座增强现代感和稳定性")
    print("- 浏览器窗口图标代表网页分析核心功能")
    print("- 升级版放大镜图标代表深度分析能力")
    print("- 金色数据分析线条代表数据流动和洞察")
    print("- 'WebAnalyzer'文字标识明确插件功能")
    print("- 装饰性圆环增强整体设计美感")

if __name__ == "__main__":
    main()