#!/usr/bin/env python3
"""
Interactive HPC Presentation Generator
Creates a stunning HTML-based interactive presentation with animations
"""

import os
import json

def create_interactive_presentation():
    """Generate interactive HTML presentation with Reveal.js"""
    
    # Create output directory
    os.makedirs('interactive_presentation', exist_ok=True)
    
    # Generate HTML file
    html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>High-Performance Computing - Interactive Presentation</title>
    
    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/black.css">
    
    <!-- Chart.js for interactive charts -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    
    <!-- Custom CSS -->
    <style>
        :root {
            --primary-color: #00d4ff;
            --secondary-color: #7b2cbf;
            --accent-color: #ff006e;
            --bg-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .reveal {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .reveal h1, .reveal h2, .reveal h3 {
            text-transform: none;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .reveal section {
            text-align: center;
        }
        
        /* Animated gradient background */
        .gradient-bg {
            background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Glowing text effect */
        .glow {
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px var(--primary-color); }
            to { text-shadow: 0 0 20px #fff, 0 0 30px var(--primary-color), 0 0 40px var(--primary-color); }
        }
        
        /* Floating animation */
        .float {
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        /* Pulse animation */
        .pulse {
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.05); opacity: 0.8; }
        }
        
        /* Rotating 3D effect */
        .rotate-3d {
            animation: rotate3d 10s linear infinite;
            transform-style: preserve-3d;
        }
        
        @keyframes rotate3d {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(360deg); }
        }
        
        /* Interactive image hover */
        .interactive-img {
            transition: all 0.3s ease;
            cursor: pointer;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        
        .interactive-img:hover {
            transform: scale(1.1) rotate(2deg);
            box-shadow: 0 10px 20px rgba(0,212,255,0.5);
        }
        
        /* Card style */
        .card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 30px rgba(0,212,255,0.3);
        }
        
        /* Timeline style */
        .timeline {
            position: relative;
            padding: 20px 0;
        }
        
        .timeline-item {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid var(--primary-color);
            border-radius: 5px;
            animation: slideInLeft 0.5s ease;
        }
        
        @keyframes slideInLeft {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        /* Chart container */
        .chart-container {
            position: relative;
            height: 400px;
            width: 100%;
            margin: 20px auto;
        }
        
        /* Icon animations */
        .icon {
            font-size: 3em;
            display: inline-block;
            margin: 10px;
            animation: bounce 2s ease infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        
        /* Grid layout */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        
        /* Comparison table */
        .comparison {
            display: flex;
            justify-content: space-around;
            align-items: stretch;
            gap: 20px;
        }
        
        .comparison-item {
            flex: 1;
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .comparison-item:hover {
            background: rgba(0,212,255,0.2);
            transform: scale(1.05);
        }
        
        /* Progress bar */
        .progress-bar {
            width: 100%;
            height: 30px;
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            overflow: hidden;
            margin: 10px 0;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            animation: fillProgress 2s ease-out;
        }
        
        @keyframes fillProgress {
            from { width: 0%; }
        }
        
        /* Particle effect background */
        #particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }
        
        /* Interactive button */
        .btn-interactive {
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            color: white;
            font-size: 1.2em;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,212,255,0.4);
        }
        
        .btn-interactive:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,212,255,0.6);
        }
        
        /* Data visualization */
        .stat-box {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
            min-width: 150px;
        }
        
        .stat-number {
            font-size: 3em;
            font-weight: bold;
            color: var(--primary-color);
            animation: countUp 2s ease-out;
        }
        
        @keyframes countUp {
            from { opacity: 0; transform: scale(0.5); }
            to { opacity: 1; transform: scale(1); }
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .grid { grid-template-columns: 1fr; }
            .comparison { flex-direction: column; }
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            
            <!-- Slide 1: Title Slide -->
            <section class="gradient-bg" data-transition="zoom">
                <h1 class="glow">High-Performance Computing</h1>
                <h2 class="float">Supercomputers and Clusters</h2>
                <div style="margin-top: 50px;">
                    <div class="icon">🚀</div>
                    <div class="icon">💻</div>
                    <div class="icon">⚡</div>
                </div>
                <p style="margin-top: 30px; font-size: 1.2em;">
                    <span class="pulse">Press → to start the journey</span>
                </p>
            </section>
            
            <!-- Slide 2: What is HPC? -->
            <section data-transition="convex">
                <h2>What is HPC? 🤔</h2>
                <div class="grid">
                    <div class="card pulse">
                        <h3>🖥️ Definition</h3>
                        <p>High-Performance Computing uses supercomputers for complex tasks</p>
                    </div>
                    <div class="card pulse" style="animation-delay: 0.2s;">
                        <h3>⚡ Power</h3>
                        <p>Handles massive data and simulations</p>
                    </div>
                    <div class="card pulse" style="animation-delay: 0.4s;">
                        <h3>🔬 Applications</h3>
                        <p>Science, research, and innovation</p>
                    </div>
                </div>
                <div style="margin-top: 30px;">
                    <canvas id="hpcChart" class="chart-container"></canvas>
                </div>
            </section>
            
            <!-- Slide 3: Brief History -->
            <section data-transition="slide">
                <h2>Brief History 📜</h2>
                <div class="timeline">
                    <div class="timeline-item" data-fragment-index="1">
                        <h3>1940s 🕰️</h3>
                        <p>Early computers emerge</p>
                    </div>
                    <div class="timeline-item" data-fragment-index="2">
                        <h3>1960s 🚀</h3>
                        <p>Supercomputers are born</p>
                    </div>
                    <div class="timeline-item" data-fragment-index="3">
                        <h3>1990s 🌐</h3>
                        <p>Clusters rise to prominence</p>
                    </div>
                    <div class="timeline-item" data-fragment-index="4">
                        <h3>2020s ⚡</h3>
                        <p>Exascale computing achieved</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 4: Why It Matters -->
            <section data-transition="zoom">
                <h2>Why It Matters 🌟</h2>
                <div class="grid">
                    <div class="card interactive-img">
                        <div class="icon">🌪️</div>
                        <h3>Weather Prediction</h3>
                        <p>Accurate forecasting saves lives</p>
                    </div>
                    <div class="card interactive-img">
                        <div class="icon">💊</div>
                        <h3>Drug Design</h3>
                        <p>Faster medical breakthroughs</p>
                    </div>
                    <div class="card interactive-img">
                        <div class="icon">🧠</div>
                        <h3>AI Training</h3>
                        <p>Powering machine learning</p>
                    </div>
                    <div class="card interactive-img">
                        <div class="icon">🌍</div>
                        <h3>Climate Modeling</h3>
                        <p>Understanding our planet</p>
                    </div>
                </div>
                <canvas id="applicationsChart" class="chart-container"></canvas>
            </section>
            
            <!-- Slide 5: Connection to Architecture -->
            <section data-transition="concave">
                <h2>Connection to Architecture 🏗️</h2>
                <div class="comparison">
                    <div class="comparison-item">
                        <h3>🔄 Parallel Processing</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 95%;"></div>
                        </div>
                        <p>Multiple tasks simultaneously</p>
                    </div>
                    <div class="comparison-item">
                        <h3>🎯 Multi-Core CPUs</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 90%;"></div>
                        </div>
                        <p>Distributed computing power</p>
                    </div>
                    <div class="comparison-item">
                        <h3>🎮 GPU Acceleration</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 98%;"></div>
                        </div>
                        <p>Massive parallel operations</p>
                    </div>
                </div>
                <div style="margin-top: 30px;">
                    <canvas id="architectureChart"></canvas>
                </div>
            </section>
            
            <!-- Slide 6: Comparing Technologies -->
            <section data-transition="zoom">
                <h2>Comparing Technologies ⚖️</h2>
                <div class="comparison">
                    <div class="comparison-item" style="background: rgba(0,212,255,0.2);">
                        <h3>🏢 Supercomputers</h3>
                        <div class="stat-box">
                            <div class="stat-number">1</div>
                            <p>Massive System</p>
                        </div>
                        <p>✅ Extreme speed</p>
                        <p>✅ Centralized</p>
                        <p>❌ Very expensive</p>
                        <p>❌ High power consumption</p>
                    </div>
                    <div class="comparison-item" style="background: rgba(255,0,110,0.2);">
                        <h3>🌐 Clusters</h3>
                        <div class="stat-box">
                            <div class="stat-number">1000+</div>
                            <p>Connected Nodes</p>
                        </div>
                        <p>✅ Scalable</p>
                        <p>✅ Cost-effective</p>
                        <p>✅ Flexible</p>
                        <p>❌ Network overhead</p>
                    </div>
                </div>
                <canvas id="comparisonChart" class="chart-container"></canvas>
            </section>
            
            <!-- Slide 7: Types of HPC -->
            <section data-transition="slide">
                <h2>Types of HPC 📊</h2>
                <div class="grid">
                    <div class="card float">
                        <h3>🔢 Vector Supercomputers</h3>
                        <p>Optimized for array operations</p>
                    </div>
                    <div class="card float" style="animation-delay: 0.3s;">
                        <h3>🔗 Massively Parallel</h3>
                        <p>Thousands of processors</p>
                    </div>
                    <div class="card float" style="animation-delay: 0.6s;">
                        <h3>🌐 Grid Computing</h3>
                        <p>Distributed resources</p>
                    </div>
                    <div class="card float" style="animation-delay: 0.9s;">
                        <h3>☁️ Cloud Clusters</h3>
                        <p>On-demand HPC</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 8: Challenges -->
            <section data-transition="convex" data-background-color="#8b0000">
                <h2>Challenges ⚠️</h2>
                <div class="grid">
                    <div class="card">
                        <h3>⚡ High Power Use</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 85%; background: #ff4444;"></div>
                        </div>
                    </div>
                    <div class="card">
                        <h3>🔥 Overheating</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 75%; background: #ff6644;"></div>
                        </div>
                    </div>
                    <div class="card">
                        <h3>📊 Data Bottlenecks</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 70%; background: #ff8844;"></div>
                        </div>
                    </div>
                    <div class="card">
                        <h3>📈 Scalability Limits</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 65%; background: #ffaa44;"></div>
                        </div>
                    </div>
                </div>
                <canvas id="challengesChart" class="chart-container"></canvas>
            </section>
            
            <!-- Slide 9: Solutions -->
            <section data-transition="zoom" data-background-color="#006400">
                <h2>Solutions ✅</h2>
                <div class="grid">
                    <div class="card pulse">
                        <h3>❄️ Advanced Cooling</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 90%; background: #44ff44;"></div>
                        </div>
                        <p>Liquid cooling systems</p>
                    </div>
                    <div class="card pulse">
                        <h3>🔋 Energy-Efficient Chips</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 85%; background: #66ff66;"></div>
                        </div>
                        <p>Low-power processors</p>
                    </div>
                    <div class="card pulse">
                        <h3>⚙️ Optimized Algorithms</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 95%; background: #88ff88;"></div>
                        </div>
                        <p>Better software efficiency</p>
                    </div>
                    <div class="card pulse">
                        <h3>🔀 Hybrid Architectures</h3>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 88%; background: #aaffaa;"></div>
                        </div>
                        <p>CPU + GPU combinations</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 10: Analysis Summary -->
            <section data-transition="slide">
                <h2>Analysis Summary 📋</h2>
                <div class="card" style="max-width: 800px; margin: 0 auto;">
                    <h3 class="glow">Key Insights</h3>
                    <div style="text-align: left; padding: 20px;">
                        <p class="fragment">✅ HPC evolves through continuous innovation</p>
                        <p class="fragment">✅ Technology comparisons drive improvements</p>
                        <p class="fragment">✅ Classifications help understand capabilities</p>
                        <p class="fragment">✅ Challenges are being systematically solved</p>
                        <p class="fragment">✅ Performance keeps improving exponentially</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 11: Recent Technologies -->
            <section data-transition="zoom">
                <h2>Recent Technologies 🆕</h2>
                <div class="grid">
                    <div class="card interactive-img rotate-3d">
                        <h3>⚡ Exascale Computing</h3>
                        <div class="stat-box">
                            <div class="stat-number">10¹⁸</div>
                            <p>FLOPS</p>
                        </div>
                        <p>Frontier Supercomputer</p>
                    </div>
                    <div class="card interactive-img">
                        <h3>🔮 Quantum Accelerators</h3>
                        <p>Quantum-classical hybrid systems</p>
                    </div>
                    <div class="card interactive-img">
                        <h3>🧠 Neuromorphic Chips</h3>
                        <p>Brain-inspired computing</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 12: Latest Research -->
            <section data-transition="convex">
                <h2>Latest Research 🔬</h2>
                <div class="timeline">
                    <div class="timeline-item">
                        <h3>🧬 AI-Driven HPC for Genomics</h3>
                        <p>Accelerating DNA sequencing and analysis</p>
                    </div>
                    <div class="timeline-item">
                        <h3>🦠 COVID-19 Modeling</h3>
                        <p>Record-breaking pandemic simulations</p>
                    </div>
                    <div class="timeline-item">
                        <h3>🌌 Universe Simulations</h3>
                        <p>Modeling billions of galaxies</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 13: More News -->
            <section data-transition="slide">
                <h2>More News 📰</h2>
                <div class="grid">
                    <div class="card pulse">
                        <h3>🌱 Green HPC Initiatives</h3>
                        <p>Sustainable data centers</p>
                        <div class="icon">♻️</div>
                    </div>
                    <div class="card pulse">
                        <h3>📡 Edge Computing Integration</h3>
                        <p>Distributed HPC at the edge</p>
                        <div class="icon">🌐</div>
                    </div>
                </div>
            </section>
            
            <!-- Slide 14: Future Trends -->
            <section data-transition="zoom">
                <h2>Future Trends 🔮</h2>
                <div class="grid">
                    <div class="card float">
                        <h3>🔬 Quantum HPC</h3>
                        <p>Quantum computing integration</p>
                    </div>
                    <div class="card float">
                        <h3>🤖 AI Fusion</h3>
                        <p>AI-optimized HPC systems</p>
                    </div>
                    <div class="card float">
                        <h3>🌿 Sustainable Designs</h3>
                        <p>Carbon-neutral computing</p>
                    </div>
                </div>
                <canvas id="trendsChart" class="chart-container"></canvas>
            </section>
            
            <!-- Slide 15: Future Directions -->
            <section data-transition="convex">
                <h2>Future Directions 🚀</h2>
                <div class="comparison">
                    <div class="comparison-item">
                        <h3>🌍 Global Collaborations</h3>
                        <p>International HPC networks</p>
                    </div>
                    <div class="comparison-item">
                        <h3>📖 Open-Source HPC</h3>
                        <p>Democratizing supercomputing</p>
                    </div>
                    <div class="comparison-item">
                        <h3>🛸 Space-Based Clusters</h3>
                        <p>Computing beyond Earth</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 16: Key Takeaways -->
            <section data-transition="slide" class="gradient-bg">
                <h2 class="glow">Key Takeaways 🎯</h2>
                <div class="card" style="max-width: 900px; margin: 0 auto;">
                    <div class="grid">
                        <div class="stat-box">
                            <div class="stat-number">⚡</div>
                            <p>HPC Powers Innovation</p>
                        </div>
                        <div class="stat-box">
                            <div class="stat-number">📈</div>
                            <p>Exponential Growth</p>
                        </div>
                        <div class="stat-box">
                            <div class="stat-number">🌍</div>
                            <p>Global Impact</p>
                        </div>
                        <div class="stat-box">
                            <div class="stat-number">🔮</div>
                            <p>Bright Future</p>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Slide 17: Real-World Impact -->
            <section data-transition="zoom">
                <h2>Real-World Impact 🌟</h2>
                <div class="grid">
                    <div class="card interactive-img">
                        <h3>🌪️ Hurricane Prediction</h3>
                        <p>Saving thousands of lives annually</p>
                    </div>
                    <div class="card interactive-img">
                        <h3>💊 Drug Discovery</h3>
                        <p>Reducing development time by years</p>
                    </div>
                    <div class="card interactive-img">
                        <h3>🌌 Universe Exploration</h3>
                        <p>Simulating cosmic phenomena</p>
                    </div>
                </div>
            </section>
            
            <!-- Slide 18: HPC in Action -->
            <section data-transition="convex">
                <h2>HPC in Action ⚙️</h2>
                <div class="card">
                    <h3>Workflow Demonstration</h3>
                    <div style="text-align: left; padding: 20px;">
                        <div class="timeline-item">
                            <strong>Step 1:</strong> Problem decomposition
                        </div>
                        <div class="timeline-item">
                            <strong>Step 2:</strong> Parallel task distribution
                        </div>
                        <div class="timeline-item">
                            <strong>Step 3:</strong> Simultaneous execution
                        </div>
                        <div class="timeline-item">
                            <strong>Step 4:</strong> Results aggregation
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Slide 19: Challenges Revisited -->
            <section data-transition="slide">
                <h2>Challenges Revisited 🔄</h2>
                <div class="comparison">
                    <div class="comparison-item">
                        <h3>🔒 Security</h3>
                        <p>Protecting sensitive computations</p>
                    </div>
                    <div class="comparison-item">
                        <h3>⚖️ Ethics in AI-HPC</h3>
                        <p>Responsible computing practices</p>
                    </div>
                </div>
                <div class="card" style="margin-top: 30px;">
                    <p>Ongoing innovations continue to address these challenges</p>
                </div>
            </section>
            
            <!-- Slide 20: Thank You & Q&A -->
            <section class="gradient-bg" data-transition="zoom">
                <h1 class="glow">Thank You! 🙏</h1>
                <h2 class="float">Questions & Answers</h2>
                <div style="margin-top: 50px;">
                    <button class="btn-interactive" onclick="alert('Thank you for attending!')">
                        Contact Me
                    </button>
                </div>
                <div style="margin-top: 30px;">
                    <div class="icon">💬</div>
                    <div class="icon">📧</div>
                    <div class="icon">🌐</div>
                </div>
                <p style="margin-top: 30px;">
                    <small>Press ESC for overview | Press F for fullscreen</small>
                </p>
            </section>
            
        </div>
    </div>
    
    <!-- Reveal.js JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
    
    <script>
        // Initialize Reveal.js
        Reveal.initialize({
            hash: true,
            transition: 'slide',
            transitionSpeed: 'default',
            backgroundTransition: 'fade',
            controls: true,
            progress: true,
            center: true,
            slideNumber: true,
            keyboard: true,
            overview: true,
            touch: true,
            loop: false,
            rtl: false,
            fragments: true,
            embedded: false,
            help: true,
            showNotes: false,
            autoPlayMedia: null,
            preloadIframes: null,
            mouseWheel: false,
            hideInactiveCursor: true,
            hideCursorTime: 5000,
            
            // Parallax background
            parallaxBackgroundImage: '',
            parallaxBackgroundSize: '',
            
            // Display presentation control arrows
            controlsTutorial: true,
            controlsLayout: 'bottom-right',
            controlsBackArrows: 'faded',
            
            // Visibility rule for backwards navigation arrows
            navigationMode: 'default',
            
            // Flags if we should show a help overlay when the question mark key is pressed
            help: true,
            
            // Flags if speaker notes should be visible to all viewers
            showNotes: false,
            
            // Global override for autoplaying embedded media (video/audio/iframe)
            autoPlayMedia: null,
            
            // Number of milliseconds between automatically proceeding to the next slide
            autoSlide: 0,
            
            // Stop auto-sliding after user input
            autoSlideStoppable: true,
            
            // Enable slide navigation via mouse wheel
            mouseWheel: false,
            
            // Hide cursor if inactive
            hideInactiveCursor: true,
            
            // Time before cursor is hidden (in ms)
            hideCursorTime: 5000,
            
            // Hides the address bar on mobile devices
            hideAddressBar: true,
            
            // Opens links in an iframe preview overlay
            previewLinks: false,
            
            // Transition style
            transition: 'slide', // none/fade/slide/convex/concave/zoom
            
            // Transition speed
            transitionSpeed: 'default', // default/fast/slow
            
            // Transition style for full page slide backgrounds
            backgroundTransition: 'fade', // none/fade/slide/convex/concave/zoom
            
            // Number of slides away from the current that are visible
            viewDistance: 3,
            
            // Number of slides away from the current that are visible on mobile devices
            mobileViewDistance: 2,
            
            // The display mode that will be used to show slides
            display: 'block',
            
            // PDF Export Options
            pdfMaxPagesPerSlide: 1,
            pdfSeparateFragments: true,
            pdfPageHeightOffset: -1
        });
        
        // Create interactive charts when slides are shown
        Reveal.on('slidechanged', event => {
            const slideIndex = event.indexh;
            
            // Slide 2: HPC Chart
            if (slideIndex === 1) {
                createHPCChart();
            }
            // Slide 4: Applications Chart
            else if (slideIndex === 3) {
                createApplicationsChart();
            }
            // Slide 5: Architecture Chart
            else if (slideIndex === 4) {
                createArchitectureChart();
            }
            // Slide 6: Comparison Chart
            else if (slideIndex === 5) {
                createComparisonChart();
            }
            // Slide 8: Challenges Chart
            else if (slideIndex === 7) {
                createChallengesChart();
            }
            // Slide 14: Trends Chart
            else if (slideIndex === 13) {
                createTrendsChart();
            }
        });
        
        // Chart creation functions
        function createHPCChart() {
            const ctx = document.getElementById('hpcChart');
            if (!ctx || ctx.chart) return;
            
            ctx.chart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Processing Power', 'Memory', 'Storage', 'Network'],
                    datasets: [{
                        data: [40, 25, 20, 15],
                        backgroundColor: [
                            'rgba(0, 212, 255, 0.8)',
                            'rgba(123, 44, 191, 0.8)',
                            'rgba(255, 0, 110, 0.8)',
                            'rgba(76, 175, 80, 0.8)'
                        ],
                        borderWidth: 2,
                        borderColor: '#fff'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            labels: { color: '#fff', font: { size: 14 } }
                        }
                    }
                }
            });
        }
        
        function createApplicationsChart() {
            const ctx = document.getElementById('applicationsChart');
            if (!ctx || ctx.chart) return;
            
            ctx.chart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: ['Weather', 'Drug Design', 'AI Training', 'Climate', 'Other'],
                    datasets: [{
                        data: [25, 20, 30, 15, 10],
                        backgroundColor: [
                            'rgba(0, 212, 255, 0.8)',
                            'rgba(255, 0, 110, 0.8)',
                            'rgba(123, 44, 191, 0.8)',
                            'rgba(76, 175, 80, 0.8)',
                            'rgba(255, 193, 7, 0.8)'
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            labels: { color: '#fff', font: { size: 14 } }
                        }
                    }
                }
            });
        }
        
        function createArchitectureChart() {
            const ctx = document.getElementById('architectureChart');
            if (!ctx || ctx.chart) return;
            
            ctx.chart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['Parallel Processing', 'Multi-Core', 'GPU', 'Memory', 'Network'],
                    datasets: [{
                        label: 'Performance',
                        data: [95, 90, 98, 85, 88],
                        backgroundColor: 'rgba(0, 212, 255, 0.2)',
                        borderColor: 'rgba(0, 212, 255, 1)',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.2)' },
                            pointLabels: { color: '#fff', font: { size: 12 } }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: { color: '#fff' }
                        }
                    }
                }
            });
        }
        
        function createComparisonChart() {
            const ctx = document.getElementById('comparisonChart');
            if (!ctx || ctx.chart) return;
            
            ctx.chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Speed', 'Cost', 'Scalability', 'Flexibility', 'Power'],
                    datasets: [{
                        label: 'Supercomputers',
                        data: [98, 20, 40, 30, 25],
                        backgroundColor: 'rgba(0, 212, 255, 0.8)'
                    }, {
                        label: 'Clusters',
                        data: [75, 80, 95, 90, 70],
                        backgroundColor: 'rgba(255, 0, 110, 0.8)'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        x: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: { color: '#fff', font: { size: 14 } }
                        }
                    }
                }
            });
        }
        
        function createChallengesChart() {
            const ctx = document.getElementById('challengesChart');
            if (!ctx || ctx.chart) return;
            
            ctx.chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Power Use', 'Overheating', 'Data Bottlenecks', 'Scalability'],
                    datasets: [{
                        label: 'Severity Level',
                        data: [85, 75, 70, 65],
                        backgroundColor: [
                            'rgba(255, 68, 68, 0.8)',
                            'rgba(255, 102, 68, 0.8)',
                            'rgba(255, 136, 68, 0.8)',
                            'rgba(255, 170, 68, 0.8)'
                        ]
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: { color: '#fff' }
                        }
                    }
                }
            });
        }
        
        function createTrendsChart() {
            const ctx = document.getElementById('trendsChart');
            if (!ctx || ctx.chart) return;
            
            ctx.chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['2025', '2028', '2031', '2034', '2037', '2040'],
                    datasets: [{
                        label: 'Computing Power (Exaflops)',
                        data: [2, 5, 12, 28, 65, 150],
                        borderColor: 'rgba(0, 212, 255, 1)',
                        backgroundColor: 'rgba(0, 212, 255, 0.2)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        x: {
                            ticks: { color: '#fff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: { color: '#fff', font: { size: 14 } }
                        }
                    }
                }
            });
        }
        
        // Initialize first chart
        setTimeout(() => {
            if (Reveal.getIndices().h === 1) {
                createHPCChart();
            }
        }, 500);
    </script>
</body>
</html>"""
    
    # Write HTML file
    output_file = 'interactive_presentation/index.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("=" * 60)
    print("INTERACTIVE HPC PRESENTATION GENERATOR")
    print("=" * 60)
    print("✅ Interactive HTML presentation created successfully!")
    print(f"📁 File: {os.path.abspath(output_file)}")
    print("\n🎨 FEATURES:")
    print("  ✓ 20 interactive slides with animations")
    print("  ✓ Animated gradient backgrounds")
    print("  ✓ Interactive charts (Chart.js)")
    print("  ✓ Hover effects on images and cards")
    print("  ✓ 3D transitions and rotations")
    print("  ✓ Floating and pulsing animations")
    print("  ✓ Timeline visualizations")
    print("  ✓ Progress bars with animations")
    print("  ✓ Responsive design")
    print("  ✓ Keyboard navigation")
    print("\n🚀 HOW TO USE:")
    print("  1. Open index.html in any modern web browser")
    print("  2. Use arrow keys (← →) to navigate")
    print("  3. Press ESC for slide overview")
    print("  4. Press F for fullscreen mode")
    print("  5. Press ? for help")
    print("\n💡 INTERACTIVE FEATURES:")
    print("  • Hover over cards to see effects")
    print("  • Charts animate when slides appear")
    print("  • Click images for interactions")
    print("  • Smooth transitions between slides")
    print("=" * 60)
    
    return output_file

if __name__ == "__main__":
    create_interactive_presentation()
