#!/usr/bin/env python3
"""
HPC Presentation Generator
Creates a professional 20-slide presentation on High-Performance Computing
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
import os

def create_gradient_background(slide, r1, g1, b1, r2, g2, b2):
    """Add a gradient background to a slide"""
    background = slide.background
    fill = background.fill
    fill.gradient()
    fill.gradient_angle = 90.0
    fill.gradient_stops[0].color.rgb = RGBColor(r1, g1, b1)
    fill.gradient_stops[1].color.rgb = RGBColor(r2, g2, b2)

def add_title_slide(prs):
    """Slide 1: Title Slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    create_gradient_background(slide, 10, 10, 40, 0, 0, 20)

    # Main title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = "Introduction to High-Performance Computing (HPC)"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(44)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 255, 255)
    title_p.alignment = PP_ALIGN.CENTER

    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(0.8))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "Supercomputers and Clusters"
    subtitle_p = subtitle_frame.paragraphs[0]
    subtitle_p.font.size = Pt(32)
    subtitle_p.font.color.rgb = RGBColor(100, 200, 255)
    subtitle_p.alignment = PP_ALIGN.CENTER

    # Add decorative elements (tech circles)
    for i in range(5):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(1 + i * 1.8), Inches(0.5 + (i % 2) * 0.3),
            Inches(0.5), Inches(0.5)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(0, 150 + i * 20, 255)
        shape.line.color.rgb = RGBColor(100, 200, 255)
        shape.line.width = Pt(2)

def add_what_is_hpc(prs):
    """Slide 2: What is HPC?"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 20, 20, 50, 10, 10, 30)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "What is HPC?"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Content
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(4))
    tf = content_box.text_frame
    tf.word_wrap = True

    points = [
        "HPC = High-Performance Computing",
        "Uses supercomputers and clusters for complex tasks",
        "Handles massive data and simulations",
        "Processes millions of calculations per second",
        "Enables breakthrough scientific discoveries"
    ]

    for i, point in enumerate(points):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = "• " + point
        p.font.size = Pt(24)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(12)
        p.level = 0

    # Add decorative boxes
    for i in range(3):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(1 + i * 2.8), Inches(5.5),
            Inches(2.2), Inches(1.2)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(30, 60, 100)
        shape.line.color.rgb = RGBColor(0, 150, 255)
        shape.line.width = Pt(2)

        labels = ["Supercomputers", "Clusters", "Parallel Processing"]
        text_frame = shape.text_frame
        text_frame.text = labels[i]
        text_frame.paragraphs[0].font.size = Pt(16)
        text_frame.paragraphs[0].font.bold = True
        text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
        text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

def add_history_slide(prs):
    """Slide 3: Brief History"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 15, 30, 50, 5, 15, 35)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Brief History of HPC"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Timeline events
    timeline = [
        ("1940s", "Early computers\n(ENIAC, UNIVAC)"),
        ("1960s", "Supercomputers emerge\n(CDC 6600)"),
        ("1990s", "Clusters rise\n(Beowulf systems)"),
        ("Today", "Exascale power\n(Frontier, Aurora)")
    ]

    for i, (year, desc) in enumerate(timeline):
        x_pos = 1 + i * 2.2

        # Timeline dot
        dot = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(x_pos + 0.7), Inches(2.5),
            Inches(0.4), Inches(0.4)
        )
        dot.fill.solid()
        dot.fill.fore_color.rgb = RGBColor(255, 200, 0)
        dot.line.width = Pt(3)
        dot.line.color.rgb = RGBColor(255, 255, 255)

        # Year label
        year_box = slide.shapes.add_textbox(Inches(x_pos + 0.2), Inches(2), Inches(1.4), Inches(0.4))
        year_frame = year_box.text_frame
        year_frame.text = year
        year_p = year_frame.paragraphs[0]
        year_p.font.size = Pt(20)
        year_p.font.bold = True
        year_p.font.color.rgb = RGBColor(255, 200, 0)
        year_p.alignment = PP_ALIGN.CENTER

        # Description
        desc_box = slide.shapes.add_textbox(Inches(x_pos), Inches(3.2), Inches(2), Inches(1.2))
        desc_frame = desc_box.text_frame
        desc_frame.text = desc
        desc_frame.word_wrap = True
        desc_p = desc_frame.paragraphs[0]
        desc_p.font.size = Pt(14)
        desc_p.font.color.rgb = RGBColor(255, 255, 255)
        desc_p.alignment = PP_ALIGN.CENTER

    # Timeline line
    line = slide.shapes.add_connector(1, Inches(1.5), Inches(2.7), Inches(9), Inches(2.7))
    line.line.color.rgb = RGBColor(100, 200, 255)
    line.line.width = Pt(3)

def add_why_it_matters(prs):
    """Slide 4: Why It Matters"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 20, 40, 60, 10, 20, 40)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Why HPC Matters"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Applications grid
    applications = [
        ("Weather\nPrediction", RGBColor(50, 150, 255)),
        ("Drug\nDesign", RGBColor(150, 50, 255)),
        ("AI Training", RGBColor(255, 100, 50)),
        ("Climate\nModeling", RGBColor(50, 255, 150)),
        ("Genomics", RGBColor(255, 200, 50)),
        ("Astrophysics", RGBColor(200, 100, 255))
    ]

    for i, (app, color) in enumerate(applications):
        row = i // 3
        col = i % 3
        x_pos = 1.2 + col * 2.8
        y_pos = 2 + row * 2.2

        # Box
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(2.4), Inches(1.8)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(2)

        # Text
        text_frame = shape.text_frame
        text_frame.text = app
        text_frame.paragraphs[0].font.size = Pt(20)
        text_frame.paragraphs[0].font.bold = True
        text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
        text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

def add_architecture_connection(prs):
    """Slide 5: Connection to Architecture"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 25, 25, 60, 15, 15, 40)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Connection to Computer Architecture"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(36)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Content
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(3.5))
    tf = content_box.text_frame

    points = [
        "Parallel Processing: Multiple operations simultaneously",
        "Multi-core CPUs: Dozens to hundreds of cores per chip",
        "GPUs: Thousands of cores for massive parallelism",
        "Distributed Memory: Shared and distributed architectures",
        "High-speed Interconnects: InfiniBand, custom fabrics",
        "Cache Hierarchies: Optimized memory access patterns"
    ]

    for i, point in enumerate(points):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = "• " + point
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(10)

    # Architecture diagram representation
    boxes = ["CPU", "GPU", "Memory", "Network"]
    colors = [RGBColor(255, 100, 100), RGBColor(100, 255, 100),
              RGBColor(100, 100, 255), RGBColor(255, 255, 100)]

    for i, (box, color) in enumerate(zip(boxes, colors)):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(1.5 + i * 1.8), Inches(5.5),
            Inches(1.5), Inches(1)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(2)

        text_frame = shape.text_frame
        text_frame.text = box
        text_frame.paragraphs[0].font.size = Pt(18)
        text_frame.paragraphs[0].font.bold = True
        text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)
        text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

def add_comparing_technologies(prs):
    """Slide 6: Comparing Technologies"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 30, 20, 50, 15, 10, 30)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Supercomputers vs. Clusters"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Comparison boxes
    # Supercomputers
    super_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.8), Inches(1.8),
        Inches(4), Inches(4.5)
    )
    super_box.fill.solid()
    super_box.fill.fore_color.rgb = RGBColor(60, 30, 100)
    super_box.line.color.rgb = RGBColor(150, 100, 255)
    super_box.line.width = Pt(3)

    super_tf = super_box.text_frame
    super_tf.text = "SUPERCOMPUTERS"
    p = super_tf.paragraphs[0]
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 200, 0)
    p.alignment = PP_ALIGN.CENTER

    super_points = [
        "• Massive scale",
        "• Centralized systems",
        "• Custom hardware",
        "• Very high cost",
        "• Peak performance",
        "• Specialized cooling"
    ]

    for point in super_points:
        p = super_tf.add_paragraph()
        p.text = point
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(8)

    # Clusters
    cluster_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(5.2), Inches(1.8),
        Inches(4), Inches(4.5)
    )
    cluster_box.fill.solid()
    cluster_box.fill.fore_color.rgb = RGBColor(30, 60, 100)
    cluster_box.line.color.rgb = RGBColor(100, 200, 255)
    cluster_box.line.width = Pt(3)

    cluster_tf = cluster_box.text_frame
    cluster_tf.text = "CLUSTERS"
    p = cluster_tf.paragraphs[0]
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = RGBColor(100, 255, 200)
    p.alignment = PP_ALIGN.CENTER

    cluster_points = [
        "• Distributed nodes",
        "• Commodity hardware",
        "• Modular design",
        "• Cost-effective",
        "• Highly scalable",
        "• Standard cooling"
    ]

    for point in cluster_points:
        p = cluster_tf.add_paragraph()
        p.text = point
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(8)

def add_types_of_hpc(prs):
    """Slide 7: Types of HPC"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 20, 35, 55, 10, 20, 35)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Types of HPC Systems"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Types with descriptions
    types = [
        ("Vector\nSupercomputers", "Single instruction,\nmultiple data", RGBColor(255, 100, 100)),
        ("Massively Parallel\nProcessors", "Thousands of\nprocessors", RGBColor(100, 255, 100)),
        ("Grid Computing", "Distributed\nresources", RGBColor(100, 150, 255)),
        ("Cloud Clusters", "Elastic, on-demand\ncomputing", RGBColor(255, 200, 100))
    ]

    for i, (type_name, desc, color) in enumerate(types):
        row = i // 2
        col = i % 2
        x_pos = 1 + col * 4.5
        y_pos = 2 + row * 2.5

        # Type box
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(3.8), Inches(2)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(3)

        # Title
        text_frame = shape.text_frame
        text_frame.text = type_name
        p = text_frame.paragraphs[0]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0, 0, 0)
        p.alignment = PP_ALIGN.CENTER

        # Description
        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = RGBColor(0, 0, 0)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(8)

def add_challenges(prs):
    """Slide 8: Challenges"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 60, 20, 20, 40, 10, 10)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "HPC Challenges"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 200, 200)

    # Challenges
    challenges = [
        ("⚡ Power\nConsumption", "Megawatts of\nelectricity"),
        ("🔥 Heat\nManagement", "Cooling systems\ncritical"),
        ("📊 Data\nBottlenecks", "I/O bandwidth\nlimits"),
        ("📈 Scalability\nLimits", "Parallel efficiency\ndecreases")
    ]

    for i, (challenge, desc) in enumerate(challenges):
        row = i // 2
        col = i % 2
        x_pos = 1.2 + col * 4.2
        y_pos = 2 + row * 2.5

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(3.6), Inches(2)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(100, 30, 30)
        shape.line.color.rgb = RGBColor(255, 100, 100)
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.text = challenge
        p = text_frame.paragraphs[0]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 200, 200)
        p.alignment = PP_ALIGN.CENTER

        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = RGBColor(255, 255, 255)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(8)

def add_solutions(prs):
    """Slide 9: Solutions"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 20, 60, 20, 10, 40, 10)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Solutions to HPC Challenges"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(150, 255, 150)

    # Solutions
    solutions = [
        ("💚 Energy\nEfficiency", "Advanced chip\ndesigns"),
        ("❄️ Advanced\nCooling", "Liquid cooling\nsystems"),
        ("⚡ Optimized\nAlgorithms", "Better data\nlocality"),
        ("🔄 Hybrid\nArchitectures", "CPU + GPU\nintegration")
    ]

    for i, (solution, desc) in enumerate(solutions):
        row = i // 2
        col = i % 2
        x_pos = 1.2 + col * 4.2
        y_pos = 2 + row * 2.5

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(3.6), Inches(2)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(30, 100, 30)
        shape.line.color.rgb = RGBColor(100, 255, 100)
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.text = solution
        p = text_frame.paragraphs[0]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = RGBColor(150, 255, 150)
        p.alignment = PP_ALIGN.CENTER

        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = RGBColor(255, 255, 255)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(8)

def add_analysis_summary(prs):
    """Slide 10: Analysis Summary"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 30, 30, 60, 15, 15, 40)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Project Analysis Summary"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Summary content
    content_box = slide.shapes.add_textbox(Inches(1.5), Inches(2), Inches(7), Inches(4))
    tf = content_box.text_frame
    tf.word_wrap = True

    summary_text = """HPC Evolution Through Multiple Lenses:

✓ Technology Comparison: Supercomputers vs. Clusters
   • Centralized power vs. distributed flexibility
   • Cost-performance trade-offs

✓ System Classification: Four major types
   • Vector, Massively Parallel, Grid, Cloud

✓ Challenge-Solution Analysis:
   • Identified critical problems (power, heat, data, scale)
   • Developed innovative solutions (efficiency, cooling, optimization)

Result: Continuous improvement driving better performance"""

    tf.text = summary_text
    for paragraph in tf.paragraphs:
        paragraph.font.size = Pt(16)
        paragraph.font.color.rgb = RGBColor(255, 255, 255)
        paragraph.space_before = Pt(8)

def add_recent_tech(prs):
    """Slide 11: Recent Technologies"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 40, 20, 60, 20, 10, 40)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Recent Technologies"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 150, 255)

    # Technologies
    techs = [
        ("Exascale Systems", "Frontier: 1.1 exaFLOPS\nAurora, El Capitan", RGBColor(255, 100, 200)),
        ("Quantum\nAccelerators", "Hybrid quantum-classical\ncomputing", RGBColor(150, 100, 255)),
        ("Neuromorphic\nChips", "Brain-inspired\narchitectures", RGBColor(100, 200, 255))
    ]

    for i, (tech, desc, color) in enumerate(techs):
        x_pos = 1.5 + i * 2.8
        y_pos = 2.5

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(2.4), Inches(3)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.text = tech
        p = text_frame.paragraphs[0]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = RGBColor(255, 255, 255)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(12)

def add_latest_research(prs):
    """Slide 12: Latest Research"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 25, 40, 55, 15, 25, 40)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Latest Research & News"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 200, 255)

    # Research items
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(5))
    tf = content_box.text_frame

    research = [
        "🧬 AI-Driven HPC for Genomics",
        "   • AlphaFold 2 protein structure prediction",
        "   • Personalized medicine breakthroughs",
        "",
        "🦠 COVID-19 Modeling",
        "   • Record-breaking pandemic simulations",
        "   • Vaccine development acceleration",
        "",
        "🌍 Climate Science",
        "   • Earth system models at unprecedented resolution",
        "   • Extreme weather prediction improvements"
    ]

    for i, line in enumerate(research):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = line
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(6)

def add_more_news(prs):
    """Slide 13: More News"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 20, 50, 40, 10, 30, 25)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Recent Developments"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(100, 255, 200)

    # News items with boxes
    news = [
        ("🌱 Green HPC\nInitiatives", "Renewable energy\npowered data centers", RGBColor(50, 150, 50)),
        ("📱 Edge Computing\nIntegration", "Distributed HPC\nat the edge", RGBColor(100, 100, 200))
    ]

    for i, (title, desc, color) in enumerate(news):
        x_pos = 1.5 + i * 3.5
        y_pos = 2.5

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(3), Inches(3)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.text = title
        p = text_frame.paragraphs[0]
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(16)
        p2.font.color.rgb = RGBColor(255, 255, 255)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(16)

def add_future_trends(prs):
    """Slide 14: Future Trends"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 30, 20, 50, 50, 30, 70)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Future Trends in HPC"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(200, 150, 255)

    # Trends
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(5))
    tf = content_box.text_frame

    trends = [
        "🔮 Quantum-HPC Fusion",
        "   • Quantum computers as HPC accelerators",
        "",
        "🤖 AI-HPC Convergence",
        "   • Machine learning optimizing HPC workflows",
        "   • HPC training next-gen AI models",
        "",
        "♻️ Sustainable Computing",
        "   • Carbon-neutral data centers by 2030",
        "   • Novel cooling technologies",
        "",
        "💊 Personalized Medicine",
        "   • Individual-level health simulations"
    ]

    for i, line in enumerate(trends):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = line
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(8)

def add_future_directions(prs):
    """Slide 15: Future Directions"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 20, 30, 60, 40, 20, 80)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Future Directions"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(150, 200, 255)

    # Directions
    directions = [
        ("🌍 Global\nCollaborations", "International HPC\nnetworks", RGBColor(100, 150, 255)),
        ("💻 Open-Source\nHPC", "Democratizing\nsupercomputing", RGBColor(255, 150, 100)),
        ("🚀 Space-Based\nClusters", "Computing in\norbit", RGBColor(200, 100, 255))
    ]

    for i, (direction, desc, color) in enumerate(directions):
        x_pos = 1.5 + i * 2.8
        y_pos = 2.5

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(2.4), Inches(3)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.text = direction
        p = text_frame.paragraphs[0]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14)
        p2.font.color.rgb = RGBColor(255, 255, 255)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(12)

def add_key_takeaways(prs):
    """Slide 16: Key Takeaways"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 35, 35, 70, 20, 20, 50)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Key Takeaways"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 200, 100)

    # Takeaways
    content_box = slide.shapes.add_textbox(Inches(1.5), Inches(2), Inches(7), Inches(4.5))
    tf = content_box.text_frame

    takeaways = [
        "🚀 HPC Powers Innovation Across All Domains",
        "",
        "📊 Evolution: From early computers to exascale systems",
        "",
        "🔄 Diverse Technologies: Supercomputers, clusters, grids, cloud",
        "",
        "⚖️ Balancing Act: Performance vs. power vs. cost",
        "",
        "🌟 Future: Quantum, AI fusion, sustainability",
        "",
        "🌍 Impact: Solving humanity's greatest challenges"
    ]

    for i, line in enumerate(takeaways):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = line
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(6)
        if line.startswith(('🚀', '📊', '🔄', '⚖️', '🌟', '🌍')):
            p.font.bold = True

def add_real_world_impact(prs):
    """Slide 17: Real-World Impact"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 40, 30, 60, 25, 15, 40)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Real-World Impact"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 180, 100)

    # Impact examples
    impacts = [
        ("🌪️ Hurricane\nPrediction", "Save lives with\naccurate forecasts", RGBColor(50, 120, 200)),
        ("💊 Drug\nDiscovery", "Faster cures for\ndiseases", RGBColor(200, 50, 150)),
        ("🌌 Universe\nSimulation", "Understanding\ncosmic origins", RGBColor(100, 50, 200))
    ]

    for i, (impact, desc, color) in enumerate(impacts):
        x_pos = 1.5 + i * 2.8
        y_pos = 2.5

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(2.4), Inches(3)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.text = impact
        p = text_frame.paragraphs[0]
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

        p2 = text_frame.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(16)
        p2.font.color.rgb = RGBColor(255, 255, 255)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(16)

def add_hpc_in_action(prs):
    """Slide 18: HPC in Action"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 30, 40, 60, 15, 25, 45)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "HPC in Action: How It Works"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(38)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(150, 255, 200)

    # Workflow diagram
    steps = [
        ("1. Problem\nDivision", RGBColor(255, 150, 150)),
        ("2. Parallel\nProcessing", RGBColor(150, 255, 150)),
        ("3. Data\nAggregation", RGBColor(150, 150, 255)),
        ("4. Results", RGBColor(255, 255, 150))
    ]

    for i, (step, color) in enumerate(steps):
        x_pos = 1 + i * 2.2
        y_pos = 2.5

        # Step box
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x_pos), Inches(y_pos),
            Inches(2), Inches(1.5)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.color.rgb = RGBColor(255, 255, 255)
        shape.line.width = Pt(2)

        text_frame = shape.text_frame
        text_frame.text = step
        text_frame.paragraphs[0].font.size = Pt(18)
        text_frame.paragraphs[0].font.bold = True
        text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)
        text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        # Arrow
        if i < 3:
            arrow = slide.shapes.add_shape(
                MSO_SHAPE.RIGHT_ARROW,
                Inches(x_pos + 2.05), Inches(y_pos + 0.6),
                Inches(0.4), Inches(0.3)
            )
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = RGBColor(255, 255, 255)
            arrow.line.color.rgb = RGBColor(200, 200, 200)

    # Speed demo info
    info_box = slide.shapes.add_textbox(Inches(1), Inches(4.5), Inches(8), Inches(1.5))
    tf = info_box.text_frame
    tf.text = "Performance Example:\n1 Computer: 100 days → 1000 Computers: 2.4 hours"
    for p in tf.paragraphs:
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 200, 100)
        p.alignment = PP_ALIGN.CENTER

def add_challenges_revisited(prs):
    """Slide 19: Challenges Revisited"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 50, 30, 50, 30, 15, 30)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Ongoing Challenges & Ethics"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(38)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 200, 255)

    # Content
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(5))
    tf = content_box.text_frame

    challenges = [
        "🔒 Security Concerns",
        "   • Protecting sensitive research data",
        "   • Preventing cyber attacks on critical infrastructure",
        "",
        "⚖️ Ethical Considerations in AI-HPC",
        "   • Bias in large-scale AI training",
        "   • Responsible use of computational power",
        "",
        "🌍 Environmental Impact",
        "   • Balancing performance with sustainability",
        "",
        "💡 Innovations Addressing These Issues",
        "   • Quantum-resistant encryption",
        "   • Transparent AI governance frameworks",
        "   • Green computing initiatives"
    ]

    for i, line in enumerate(challenges):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = line
        p.font.size = Pt(18)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.space_before = Pt(6)
        if line.startswith(('🔒', '⚖️', '🌍', '💡')):
            p.font.bold = True

def add_thank_you(prs):
    """Slide 20: Thank You & Q&A"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    create_gradient_background(slide, 30, 10, 50, 60, 20, 80)

    # Main thank you
    title_box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = "Thank You!"
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(60)
    title_p.font.bold = True
    title_p.font.color.rgb = RGBColor(255, 220, 100)
    title_p.alignment = PP_ALIGN.CENTER

    # Q&A
    qa_box = slide.shapes.add_textbox(Inches(1), Inches(3.8), Inches(8), Inches(1))
    qa_frame = qa_box.text_frame
    qa_frame.text = "Questions & Answers"
    qa_p = qa_frame.paragraphs[0]
    qa_p.font.size = Pt(40)
    qa_p.font.bold = True
    qa_p.font.color.rgb = RGBColor(150, 220, 255)
    qa_p.alignment = PP_ALIGN.CENTER

    # Contact info placeholder
    contact_box = slide.shapes.add_textbox(Inches(2), Inches(5.5), Inches(6), Inches(1))
    contact_frame = contact_box.text_frame
    contact_frame.text = "Contact: [Your Name]\n[Your Email/Institution]"
    for p in contact_frame.paragraphs:
        p.font.size = Pt(18)
        p.font.color.rgb = RGBColor(200, 200, 200)
        p.alignment = PP_ALIGN.CENTER

    # Decorative circles
    for i in range(8):
        circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(1 + i * 1.1), Inches(0.5 + (i % 2) * 0.4),
            Inches(0.4), Inches(0.4)
        )
        circle.fill.solid()
        circle.fill.fore_color.rgb = RGBColor(255, 220 - i * 10, 100 + i * 10)
        circle.line.width = Pt(0)

def main():
    """Main function to create the HPC presentation"""
    print("Creating HPC Presentation...")

    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Add all slides
    print("Adding Slide 1: Title Slide")
    add_title_slide(prs)

    print("Adding Slide 2: What is HPC?")
    add_what_is_hpc(prs)

    print("Adding Slide 3: Brief History")
    add_history_slide(prs)

    print("Adding Slide 4: Why It Matters")
    add_why_it_matters(prs)

    print("Adding Slide 5: Connection to Architecture")
    add_architecture_connection(prs)

    print("Adding Slide 6: Comparing Technologies")
    add_comparing_technologies(prs)

    print("Adding Slide 7: Types of HPC")
    add_types_of_hpc(prs)

    print("Adding Slide 8: Challenges")
    add_challenges(prs)

    print("Adding Slide 9: Solutions")
    add_solutions(prs)

    print("Adding Slide 10: Analysis Summary")
    add_analysis_summary(prs)

    print("Adding Slide 11: Recent Technologies")
    add_recent_tech(prs)

    print("Adding Slide 12: Latest Research")
    add_latest_research(prs)

    print("Adding Slide 13: More News")
    add_more_news(prs)

    print("Adding Slide 14: Future Trends")
    add_future_trends(prs)

    print("Adding Slide 15: Future Directions")
    add_future_directions(prs)

    print("Adding Slide 16: Key Takeaways")
    add_key_takeaways(prs)

    print("Adding Slide 17: Real-World Impact")
    add_real_world_impact(prs)

    print("Adding Slide 18: HPC in Action")
    add_hpc_in_action(prs)

    print("Adding Slide 19: Challenges Revisited")
    add_challenges_revisited(prs)

    print("Adding Slide 20: Thank You & Q&A")
    add_thank_you(prs)

    # Save presentation
    output_file = "/vercel/sandbox/HPC_Presentation.pptx"
    prs.save(output_file)
    print(f"\n✅ Presentation created successfully: {output_file}")
    print(f"📊 Total slides: {len(prs.slides)}")

    return output_file

if __name__ == "__main__":
    main()
