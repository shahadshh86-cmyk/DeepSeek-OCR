#!/usr/bin/env python3
"""
HPC Presentation Generator
Creates a stunning 20-slide presentation on High-Performance Computing
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image, ImageDraw, ImageFont
import io
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class HPCPresentationGenerator:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width = Inches(10)
        self.prs.slide_height = Inches(7.5)
        
        # Color scheme - Tech/HPC themed
        self.colors = {
            'primary': RGBColor(0, 120, 215),      # Blue
            'secondary': RGBColor(0, 180, 240),    # Light Blue
            'accent': RGBColor(255, 185, 0),       # Gold
            'dark': RGBColor(20, 30, 48),          # Dark Blue
            'light': RGBColor(240, 248, 255),      # Alice Blue
            'success': RGBColor(16, 185, 129),     # Green
            'warning': RGBColor(245, 158, 11),     # Orange
            'danger': RGBColor(239, 68, 68),       # Red
            'white': RGBColor(255, 255, 255),
            'silver': RGBColor(192, 192, 192)
        }
        
    def add_background_gradient(self, slide, color1, color2):
        """Add a gradient background to slide"""
        background = slide.background
        fill = background.fill
        fill.gradient()
        fill.gradient_angle = 45
        fill.gradient_stops[0].color.rgb = color1
        fill.gradient_stops[1].color.rgb = color2
        
    def add_title_slide(self):
        """Slide 1: Title Slide"""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])  # Blank layout
        self.add_background_gradient(slide, self.colors['dark'], self.colors['primary'])
        
        # Main title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
        title_frame = title_box.text_frame
        title_frame.text = "Introduction to High-Performance Computing (HPC)"
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(54)
        title_para.font.bold = True
        title_para.font.color.rgb = self.colors['white']
        title_para.alignment = PP_ALIGN.CENTER
        
        # Subtitle
        subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(0.8))
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.text = "Supercomputers and Clusters"
        subtitle_para = subtitle_frame.paragraphs[0]
        subtitle_para.font.size = Pt(36)
        subtitle_para.font.color.rgb = self.colors['accent']
        subtitle_para.alignment = PP_ALIGN.CENTER
        
        # Footer info
        footer_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(9), Inches(0.5))
        footer_frame = footer_box.text_frame
        footer_frame.text = "Computer Organization and Architecture | November 2025"
        footer_para = footer_frame.paragraphs[0]
        footer_para.font.size = Pt(18)
        footer_para.font.color.rgb = self.colors['silver']
        footer_para.alignment = PP_ALIGN.CENTER
        
    def add_content_slide(self, title, content_items, slide_number):
        """Add a content slide with title and bullet points"""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        self.add_background_gradient(slide, self.colors['light'], self.colors['white'])
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(40)
        title_para.font.bold = True
        title_para.font.color.rgb = self.colors['primary']
        
        # Decorative line
        line = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.5), Inches(1.1), Inches(9), Inches(0.05)
        )
        line.fill.solid()
        line.fill.fore_color.rgb = self.colors['accent']
        line.line.fill.background()
        
        # Content
        content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(8.4), Inches(5.5))
        text_frame = content_box.text_frame
        text_frame.word_wrap = True
        
        for i, item in enumerate(content_items):
            if i > 0:
                text_frame.add_paragraph()
            p = text_frame.paragraphs[i]
            p.text = f"• {item}"
            p.font.size = Pt(24)
            p.font.color.rgb = self.colors['dark']
            p.space_after = Pt(12)
            p.level = 0
            
        # Slide number
        slide_num_box = slide.shapes.add_textbox(Inches(9.2), Inches(7), Inches(0.5), Inches(0.3))
        slide_num_frame = slide_num_box.text_frame
        slide_num_frame.text = str(slide_number)
        slide_num_para = slide_num_frame.paragraphs[0]
        slide_num_para.font.size = Pt(14)
        slide_num_para.font.color.rgb = self.colors['primary']
        slide_num_para.alignment = PP_ALIGN.RIGHT
        
        return slide
        
    def create_architecture_diagram(self):
        """Create HPC architecture diagram"""
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        # Draw components
        components = [
            {'name': 'CPU Cores', 'pos': (1, 4), 'color': '#0078D7'},
            {'name': 'GPU Units', 'pos': (3.5, 4), 'color': '#00B4D8'},
            {'name': 'Memory', 'pos': (6, 4), 'color': '#FFB900'},
            {'name': 'Storage', 'pos': (8.5, 4), 'color': '#10B981'},
            {'name': 'Network', 'pos': (4.5, 1.5), 'color': '#EF4444'}
        ]
        
        for comp in components:
            rect = patches.FancyBboxPatch(
                (comp['pos'][0] - 0.8, comp['pos'][1] - 0.4),
                1.6, 0.8,
                boxstyle="round,pad=0.1",
                facecolor=comp['color'],
                edgecolor='black',
                linewidth=2
            )
            ax.add_patch(rect)
            ax.text(comp['pos'][0], comp['pos'][1], comp['name'],
                   ha='center', va='center', fontsize=12, color='white', weight='bold')
        
        # Draw connections
        connections = [
            ((1.8, 4), (2.7, 4)),
            ((4.3, 4), (5.2, 4)),
            ((6.8, 4), (7.7, 4)),
            ((2.5, 3.6), (4.5, 2.3)),
            ((5.5, 3.6), (4.5, 2.3))
        ]
        
        for conn in connections:
            ax.plot([conn[0][0], conn[1][0]], [conn[0][1], conn[1][1]],
                   'k-', linewidth=2, alpha=0.6)
        
        ax.text(5, 5.5, 'HPC Architecture', ha='center', fontsize=18, weight='bold')
        
        # Save to bytes
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_timeline_diagram(self):
        """Create HPC history timeline"""
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 4)
        ax.axis('off')
        
        timeline_data = [
            {'year': '1940s', 'event': 'Early Computers', 'pos': 1.5},
            {'year': '1960s', 'event': 'Supercomputers', 'pos': 4},
            {'year': '1990s', 'event': 'Clusters Rise', 'pos': 7},
            {'year': '2020s', 'event': 'Exascale Era', 'pos': 10}
        ]
        
        # Draw timeline line
        ax.plot([1, 11], [2, 2], 'k-', linewidth=3)
        
        colors = ['#0078D7', '#00B4D8', '#FFB900', '#10B981']
        
        for i, item in enumerate(timeline_data):
            # Draw point
            circle = plt.Circle((item['pos'], 2), 0.15, color=colors[i], zorder=10)
            ax.add_patch(circle)
            
            # Add year
            ax.text(item['pos'], 2.8, item['year'], ha='center', fontsize=14, weight='bold')
            
            # Add event
            ax.text(item['pos'], 1.2, item['event'], ha='center', fontsize=12)
        
        ax.text(6, 3.5, 'HPC Evolution Timeline', ha='center', fontsize=16, weight='bold')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_comparison_chart(self):
        """Create supercomputer vs cluster comparison"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        categories = ['Speed', 'Cost', 'Scalability', 'Flexibility', 'Maintenance']
        supercomputer = [9, 3, 6, 5, 4]
        cluster = [7, 8, 9, 8, 7]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, supercomputer, width, label='Supercomputer',
                      color='#0078D7', alpha=0.8)
        bars2 = ax.bar(x + width/2, cluster, width, label='Cluster',
                      color='#10B981', alpha=0.8)
        
        ax.set_ylabel('Rating (0-10)', fontsize=12, weight='bold')
        ax.set_title('Supercomputers vs Clusters Comparison', fontsize=16, weight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=11)
        ax.legend(fontsize=12)
        ax.set_ylim(0, 10)
        ax.grid(axis='y', alpha=0.3)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_types_diagram(self):
        """Create HPC types classification"""
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        # Root
        root = patches.FancyBboxPatch((3.5, 5.5), 3, 0.8,
                                     boxstyle="round,pad=0.1",
                                     facecolor='#0078D7',
                                     edgecolor='black', linewidth=2)
        ax.add_patch(root)
        ax.text(5, 5.9, 'HPC Systems', ha='center', va='center',
               fontsize=14, color='white', weight='bold')
        
        # Types
        types = [
            {'name': 'Vector\nSupercomputers', 'pos': (0.5, 3)},
            {'name': 'Massively\nParallel', 'pos': (3, 3)},
            {'name': 'Grid\nComputing', 'pos': (5.5, 3)},
            {'name': 'Cloud\nClusters', 'pos': (8, 3)}
        ]
        
        colors = ['#00B4D8', '#FFB900', '#10B981', '#EF4444']
        
        for i, t in enumerate(types):
            rect = patches.FancyBboxPatch(
                (t['pos'][0] - 0.9, t['pos'][1] - 0.5),
                1.8, 1,
                boxstyle="round,pad=0.1",
                facecolor=colors[i],
                edgecolor='black',
                linewidth=2
            )
            ax.add_patch(rect)
            ax.text(t['pos'][0], t['pos'][1], t['name'],
                   ha='center', va='center', fontsize=11, color='white', weight='bold')
            
            # Connection lines
            ax.plot([5, t['pos'][0]], [5.5, 3.5], 'k-', linewidth=2, alpha=0.5)
        
        ax.text(5, 6.5, 'HPC Types Classification', ha='center', fontsize=16, weight='bold')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_challenges_diagram(self):
        """Create challenges visualization"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        challenges = ['Power\nConsumption', 'Overheating', 'Data\nBottlenecks', 'Scalability\nLimits']
        values = [85, 75, 70, 65]
        colors_list = ['#EF4444', '#F59E0B', '#FFB900', '#FF6B6B']
        
        bars = ax.barh(challenges, values, color=colors_list, alpha=0.8, edgecolor='black', linewidth=2)
        
        ax.set_xlabel('Severity Level (%)', fontsize=12, weight='bold')
        ax.set_title('HPC Challenges', fontsize=16, weight='bold', pad=20)
        ax.set_xlim(0, 100)
        ax.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val + 2, i, f'{val}%', va='center', fontsize=11, weight='bold')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_solutions_diagram(self):
        """Create solutions visualization"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        solutions = ['Advanced\nCooling', 'Energy-Efficient\nChips', 'Optimized\nAlgorithms', 'Hybrid\nArchitectures']
        effectiveness = [90, 85, 80, 88]
        colors_list = ['#10B981', '#059669', '#34D399', '#6EE7B7']
        
        bars = ax.barh(solutions, effectiveness, color=colors_list, alpha=0.8, edgecolor='black', linewidth=2)
        
        ax.set_xlabel('Effectiveness (%)', fontsize=12, weight='bold')
        ax.set_title('HPC Solutions', fontsize=16, weight='bold', pad=20)
        ax.set_xlim(0, 100)
        ax.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, effectiveness)):
            ax.text(val + 2, i, f'{val}%', va='center', fontsize=11, weight='bold')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_applications_diagram(self):
        """Create applications pie chart"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        applications = ['Weather\nPrediction', 'Drug\nDesign', 'AI\nTraining', 'Climate\nModeling', 'Genomics', 'Physics\nSimulation']
        sizes = [18, 16, 25, 15, 14, 12]
        colors_list = ['#0078D7', '#00B4D8', '#FFB900', '#10B981', '#EF4444', '#8B5CF6']
        explode = (0.05, 0.05, 0.1, 0.05, 0.05, 0.05)
        
        wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=applications,
                                          colors=colors_list, autopct='%1.1f%%',
                                          shadow=True, startangle=90,
                                          textprops={'fontsize': 12, 'weight': 'bold'})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(11)
            autotext.set_weight('bold')
        
        ax.set_title('HPC Applications Distribution', fontsize=16, weight='bold', pad=20)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def create_future_trends_diagram(self):
        """Create future trends visualization"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        years = ['2025', '2027', '2030', '2035', '2040']
        quantum_hpc = [10, 25, 45, 70, 90]
        ai_fusion = [30, 50, 70, 85, 95]
        sustainable = [20, 40, 60, 80, 92]
        
        ax.plot(years, quantum_hpc, marker='o', linewidth=3, markersize=10,
               label='Quantum HPC', color='#8B5CF6')
        ax.plot(years, ai_fusion, marker='s', linewidth=3, markersize=10,
               label='AI Fusion', color='#0078D7')
        ax.plot(years, sustainable, marker='^', linewidth=3, markersize=10,
               label='Sustainable Design', color='#10B981')
        
        ax.set_xlabel('Year', fontsize=12, weight='bold')
        ax.set_ylabel('Adoption Rate (%)', fontsize=12, weight='bold')
        ax.set_title('Future HPC Trends Projection', fontsize=16, weight='bold', pad=20)
        ax.legend(fontsize=11, loc='upper left')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 100)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        plt.close()
        return buf
        
    def add_slide_with_image(self, title, content_items, image_buffer, slide_number):
        """Add slide with content and image"""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        self.add_background_gradient(slide, self.colors['light'], self.colors['white'])
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(40)
        title_para.font.bold = True
        title_para.font.color.rgb = self.colors['primary']
        
        # Decorative line
        line = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.5), Inches(1.1), Inches(9), Inches(0.05)
        )
        line.fill.solid()
        line.fill.fore_color.rgb = self.colors['accent']
        line.line.fill.background()
        
        # Content (left side)
        if content_items:
            content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(4), Inches(5.5))
            text_frame = content_box.text_frame
            text_frame.word_wrap = True
            
            for i, item in enumerate(content_items):
                if i > 0:
                    text_frame.add_paragraph()
                p = text_frame.paragraphs[i]
                p.text = f"• {item}"
                p.font.size = Pt(20)
                p.font.color.rgb = self.colors['dark']
                p.space_after = Pt(10)
        
        # Image (right side)
        if image_buffer:
            pic = slide.shapes.add_picture(image_buffer, Inches(5.2), Inches(1.8),
                                          width=Inches(4.3), height=Inches(4.8))
        
        # Slide number
        slide_num_box = slide.shapes.add_textbox(Inches(9.2), Inches(7), Inches(0.5), Inches(0.3))
        slide_num_frame = slide_num_box.text_frame
        slide_num_frame.text = str(slide_number)
        slide_num_para = slide_num_frame.paragraphs[0]
        slide_num_para.font.size = Pt(14)
        slide_num_para.font.color.rgb = self.colors['primary']
        slide_num_para.alignment = PP_ALIGN.RIGHT
        
    def add_image_focused_slide(self, title, image_buffer, caption, slide_number):
        """Add slide with large centered image"""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        self.add_background_gradient(slide, self.colors['light'], self.colors['white'])
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(40)
        title_para.font.bold = True
        title_para.font.color.rgb = self.colors['primary']
        title_para.alignment = PP_ALIGN.CENTER
        
        # Image
        if image_buffer:
            pic = slide.shapes.add_picture(image_buffer, Inches(1), Inches(1.5),
                                          width=Inches(8), height=Inches(5))
        
        # Caption
        if caption:
            caption_box = slide.shapes.add_textbox(Inches(1), Inches(6.7), Inches(8), Inches(0.5))
            caption_frame = caption_box.text_frame
            caption_frame.text = caption
            caption_para = caption_frame.paragraphs[0]
            caption_para.font.size = Pt(18)
            caption_para.font.italic = True
            caption_para.font.color.rgb = self.colors['dark']
            caption_para.alignment = PP_ALIGN.CENTER
        
        # Slide number
        slide_num_box = slide.shapes.add_textbox(Inches(9.2), Inches(7), Inches(0.5), Inches(0.3))
        slide_num_frame = slide_num_box.text_frame
        slide_num_frame.text = str(slide_number)
        slide_num_para = slide_num_frame.paragraphs[0]
        slide_num_para.font.size = Pt(14)
        slide_num_para.font.color.rgb = self.colors['primary']
        
    def add_thank_you_slide(self):
        """Slide 20: Thank You & Q&A"""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        self.add_background_gradient(slide, self.colors['primary'], self.colors['dark'])
        
        # Thank you text
        thank_you_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
        thank_you_frame = thank_you_box.text_frame
        thank_you_frame.text = "Thank You!"
        thank_you_para = thank_you_frame.paragraphs[0]
        thank_you_para.font.size = Pt(72)
        thank_you_para.font.bold = True
        thank_you_para.font.color.rgb = self.colors['white']
        thank_you_para.alignment = PP_ALIGN.CENTER
        
        # Q&A text
        qa_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(0.8))
        qa_frame = qa_box.text_frame
        qa_frame.text = "Questions & Answers"
        qa_para = qa_frame.paragraphs[0]
        qa_para.font.size = Pt(36)
        qa_para.font.color.rgb = self.colors['accent']
        qa_para.alignment = PP_ALIGN.CENTER
        
        # Contact info
        contact_box = slide.shapes.add_textbox(Inches(0.5), Inches(6), Inches(9), Inches(0.8))
        contact_frame = contact_box.text_frame
        contact_frame.text = "For more information: hpc-research@university.edu"
        contact_para = contact_frame.paragraphs[0]
        contact_para.font.size = Pt(18)
        contact_para.font.color.rgb = self.colors['silver']
        contact_para.alignment = PP_ALIGN.CENTER
        
    def generate_presentation(self):
        """Generate the complete presentation"""
        print("🚀 Generating HPC Presentation...")
        
        # Slide 1: Title
        print("  ✓ Creating Slide 1: Title Slide")
        self.add_title_slide()
        
        # Slide 2: What is HPC?
        print("  ✓ Creating Slide 2: What is HPC?")
        self.add_content_slide(
            "What is HPC?",
            [
                "HPC = High-Performance Computing",
                "Uses supercomputers and clusters for complex computational tasks",
                "Handles massive datasets and simulations",
                "Processes calculations at unprecedented speeds",
                "Essential for solving problems beyond traditional computing"
            ],
            2
        )
        
        # Slide 3: Brief History
        print("  ✓ Creating Slide 3: Brief History")
        timeline_img = self.create_timeline_diagram()
        self.add_image_focused_slide(
            "Brief History of HPC",
            timeline_img,
            "Evolution from early computers to exascale supercomputers",
            3
        )
        
        # Slide 4: Why It Matters
        print("  ✓ Creating Slide 4: Why It Matters")
        apps_img = self.create_applications_diagram()
        self.add_slide_with_image(
            "Why HPC Matters",
            [
                "Solves complex real-world problems",
                "Weather prediction & climate modeling",
                "Drug discovery & molecular design",
                "AI training & deep learning",
                "Scientific research & simulations"
            ],
            apps_img,
            4
        )
        
        # Slide 5: Connection to Architecture
        print("  ✓ Creating Slide 5: Connection to Architecture")
        arch_img = self.create_architecture_diagram()
        self.add_slide_with_image(
            "Connection to Computer Architecture",
            [
                "Parallel processing fundamentals",
                "Multi-core CPUs & GPUs",
                "Distributed memory systems",
                "High-speed interconnects",
                "Cache hierarchies & optimization"
            ],
            arch_img,
            5
        )
        
        # Slide 6: Comparing Technologies
        print("  ✓ Creating Slide 6: Comparing Technologies")
        comparison_img = self.create_comparison_chart()
        self.add_image_focused_slide(
            "Supercomputers vs Clusters",
            comparison_img,
            "Comparing performance, cost, scalability, and flexibility",
            6
        )
        
        # Slide 7: Types of HPC
        print("  ✓ Creating Slide 7: Types of HPC")
        types_img = self.create_types_diagram()
        self.add_image_focused_slide(
            "Types of HPC Systems",
            types_img,
            "Classification of HPC architectures and approaches",
            7
        )
        
        # Slide 8: Challenges
        print("  ✓ Creating Slide 8: Challenges")
        challenges_img = self.create_challenges_diagram()
        self.add_slide_with_image(
            "HPC Challenges",
            [
                "High power consumption",
                "Thermal management issues",
                "Data transfer bottlenecks",
                "Scalability limitations",
                "Programming complexity"
            ],
            challenges_img,
            8
        )
        
        # Slide 9: Solutions
        print("  ✓ Creating Slide 9: Solutions")
        solutions_img = self.create_solutions_diagram()
        self.add_slide_with_image(
            "Solutions to HPC Challenges",
            [
                "Advanced liquid cooling systems",
                "Energy-efficient chip designs",
                "Optimized algorithms & compilers",
                "Hybrid CPU-GPU architectures",
                "Improved interconnect technologies"
            ],
            solutions_img,
            9
        )
        
        # Slide 10: Analysis Summary
        print("  ✓ Creating Slide 10: Analysis Summary")
        self.add_content_slide(
            "Project Analysis Summary",
            [
                "HPC evolves through continuous innovation",
                "Technology comparisons drive improvements",
                "Classification helps understand diverse approaches",
                "Challenges are systematically addressed",
                "Performance gains enable new discoveries"
            ],
            10
        )
        
        # Slide 11: Recent Technologies
        print("  ✓ Creating Slide 11: Recent Technologies")
        self.add_content_slide(
            "Recent HPC Technologies",
            [
                "Exascale supercomputers (e.g., Frontier, Aurora)",
                "Quantum computing accelerators",
                "Neuromorphic computing chips",
                "AI-optimized hardware (TPUs, NPUs)",
                "Advanced memory technologies (HBM, CXL)"
            ],
            11
        )
        
        # Slide 12: Latest Research
        print("  ✓ Creating Slide 12: Latest Research")
        self.add_content_slide(
            "Latest HPC Research",
            [
                "AI-driven HPC for genomics and proteomics",
                "Record-breaking COVID-19 modeling simulations",
                "Fusion energy research breakthroughs",
                "Climate change prediction improvements",
                "Materials science discoveries"
            ],
            12
        )
        
        # Slide 13: More News
        print("  ✓ Creating Slide 13: More News")
        self.add_content_slide(
            "Recent HPC Developments",
            [
                "Green HPC initiatives reducing carbon footprint",
                "Edge computing integration with HPC",
                "Open-source HPC software ecosystems",
                "Cloud-based HPC services expansion",
                "International HPC collaborations"
            ],
            13
        )
        
        # Slide 14: Future Trends
        print("  ✓ Creating Slide 14: Future Trends")
        trends_img = self.create_future_trends_diagram()
        self.add_slide_with_image(
            "Future HPC Trends",
            [
                "Quantum-classical hybrid systems",
                "AI and HPC convergence",
                "Sustainable computing designs",
                "Ubiquitous HPC access",
                "Personalized medicine platforms"
            ],
            trends_img,
            14
        )
        
        # Slide 15: Future Directions
        print("  ✓ Creating Slide 15: Future Directions")
        self.add_content_slide(
            "Future HPC Directions",
            [
                "Global collaborative research networks",
                "Open-source HPC democratization",
                "Space-based computing clusters",
                "Biological computing integration",
                "Autonomous HPC systems"
            ],
            15
        )
        
        # Slide 16: Key Takeaways
        print("  ✓ Creating Slide 16: Key Takeaways")
        self.add_content_slide(
            "Key Takeaways",
            [
                "HPC powers scientific and technological innovation",
                "Evolution from mainframes to exascale systems",
                "Tackles humanity's most complex challenges",
                "Continuous advancement in hardware and software",
                "Critical for future discoveries and breakthroughs"
            ],
            16
        )
        
        # Slide 17: Real-World Impact
        print("  ✓ Creating Slide 17: Real-World Impact")
        self.add_content_slide(
            "Real-World HPC Impact",
            [
                "Hurricane prediction saves thousands of lives",
                "Drug discovery accelerated from years to months",
                "Universe simulations reveal cosmic mysteries",
                "Protein folding breakthroughs (AlphaFold)",
                "Climate models guide policy decisions"
            ],
            17
        )
        
        # Slide 18: HPC in Action
        print("  ✓ Creating Slide 18: HPC in Action")
        self.add_content_slide(
            "HPC in Action",
            [
                "Parallel task distribution across thousands of nodes",
                "Real-time data processing at petabyte scale",
                "Speedup: Days → Hours → Minutes",
                "Workflow: Problem → Decomposition → Parallel Execution → Results",
                "Example: Weather forecast in 30 minutes for 7-day prediction"
            ],
            18
        )
        
        # Slide 19: Challenges Revisited
        print("  ✓ Creating Slide 19: Challenges Revisited")
        self.add_content_slide(
            "Ongoing Challenges & Ethics",
            [
                "Cybersecurity in distributed systems",
                "Ethical AI in HPC applications",
                "Energy sustainability concerns",
                "Digital divide and access inequality",
                "Responsible use of computational power"
            ],
            19
        )
        
        # Slide 20: Thank You
        print("  ✓ Creating Slide 20: Thank You & Q&A")
        self.add_thank_you_slide()
        
        # Save presentation
        output_file = "/vercel/sandbox/HPC_Presentation.pptx"
        self.prs.save(output_file)
        print(f"\n✅ Presentation saved successfully: {output_file}")
        print(f"📊 Total slides: {len(self.prs.slides)}")
        return output_file

def main():
    """Main function"""
    print("=" * 60)
    print("HPC PRESENTATION GENERATOR")
    print("=" * 60)
    
    generator = HPCPresentationGenerator()
    output_file = generator.generate_presentation()
    
    print("\n" + "=" * 60)
    print("🎉 PRESENTATION GENERATION COMPLETE!")
    print("=" * 60)
    print(f"\n📁 File: {output_file}")
    print("📝 Slides: 20")
    print("🎨 Features: Gradients, diagrams, charts, professional styling")
    print("\n💡 Open the file in PowerPoint, LibreOffice, or Google Slides")
    print("=" * 60)

if __name__ == "__main__":
    main()
