"""
Syllabus functions for seeding the database.
Handles creation and population of syllabus modules, topics, and
detailed content.
"""
import json
import os
from modules.syllabus.service import SyllabusService
from models import Certification, SyllabusModule
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from .frontend_topic_mapping import MODULE1_TOPICS, MODULE2_TOPICS, MODULE3_TOPICS, TOPIC_MAPPING


async def create_frontend_react_syllabus(session, certification_map):
    """Create syllabus structure for Frontend React Fundamentals"""
    print("📚 Creating Frontend React Fundamentals syllabus...")
    
    try:
        # Get the certification
        certification = certification_map.get("frontend-react-fundamentals")
        if not certification:
            print("⚠️  Frontend React Fundamentals certification not found!")
            return
        
        # Check if certification has syllabus content
        if not certification.syllabus:
            print("⚠️  No syllabus content found in certification!")
            return
        
        syllabus_service = SyllabusService()
        
        # Parse the JSON syllabus content
        try:
            syllabus_data = json.loads(certification.syllabus)
        except (json.JSONDecodeError, TypeError) as e:
            print(f"❌ Error parsing syllabus JSON: {e}")
            return
        
        # Get modules from the JSON data
        modules = syllabus_data.get("modules", [])
        if not modules:
            print("⚠️  No modules found in syllabus data!")
            return
        
        print(f"📖 Found {len(modules)} modules in syllabus JSON")
        
        # Create modules and topics from JSON data
        for module_data in modules:
            # Create module
            module_info = {
                "module_number": module_data.get("moduleNumber", 1),
                "title": module_data.get("title", "Untitled Module"),
                "description": module_data.get("duration", ""),
                "duration": module_data.get("duration", ""),
                "order_index": module_data.get("moduleNumber", 1) - 1,
                "learning_objectives": (
                    module_data.get("learningObjectives", [])
                )
            }
            
            module = await syllabus_service.create_module(
                session, certification.id, module_info
            )
            
            # Create topics for this module
            topics = module_data.get("topics", [])
            topic_count = 0
            
            for i, topic in enumerate(topics):
                # Handle both string and object topics
                if isinstance(topic, str):
                    module_num = module_data.get('moduleNumber', 1)
                    desc = f"Topic {i + 1} from Module {module_num}"
                    topic_data = {
                        "title": topic,
                        "description": desc,
                        "introduction": "",
                        "order_index": i,
                        "estimated_duration": "15 minutes"
                    }
                elif isinstance(topic, dict):
                    topic_data = {
                        "title": topic.get("title", f"Topic {i + 1}"),
                        "description": topic.get("title", f"Topic {i + 1}"),
                        "introduction": "",
                        "order_index": i,
                        "estimated_duration": "15 minutes"
                    }
                    
                    # If topic has detailed content, extract introduction
                    has_content = (
                        "content" in topic and
                        isinstance(topic["content"], dict)
                    )
                    if has_content:
                        topic_data["introduction"] = (
                            topic["content"].get("introduction", "")
                        )
                else:
                    continue  # Skip invalid topic format
                
                await syllabus_service.create_topic(
                    session, module.id, topic_data
                )
                topic_count += 1
            
            mod_num = module_data.get('moduleNumber', '?')
            mod_title = module_info['title']
            print(
                f"✅ Created Module {mod_num}: {mod_title} with "
                f"{topic_count} topics"
            )
        
    except Exception as e:
        print(f"❌ Error creating syllabus: {e}")
        import traceback
        traceback.print_exc()


async def create_system_design_syllabus(session, certification_map):
    """Create syllabus structure for System Design Fundamentals"""
    print("📚 Creating System Design Fundamentals syllabus...")
    
    try:
        # Get the certification
        certification = certification_map.get("system-design-fundamentals")
        if not certification:
            print("⚠️  System Design Fundamentals certification not found!")
            return
        
        # Check if certification has syllabus content
        if not certification.syllabus:
            print("⚠️  No syllabus content found in certification!")
            return
        
        syllabus_service = SyllabusService()
        
        # Parse the JSON syllabus content
        try:
            syllabus_data = json.loads(certification.syllabus)
        except (json.JSONDecodeError, TypeError) as e:
            print(f"❌ Error parsing syllabus JSON: {e}")
            return
        
        # Get modules from the JSON data
        modules = syllabus_data.get("modules", [])
        if not modules:
            print("⚠️  No modules found in syllabus data!")
            return
        
        print(f"📖 Found {len(modules)} modules in syllabus JSON")
        
        # Create modules and topics from JSON data
        for module_data in modules:
            # Create module
            module_info = {
                "module_number": module_data.get("moduleNumber", 1),
                "title": module_data.get("title", "Untitled Module"),
                "description": module_data.get("duration", ""),
                "duration": module_data.get("duration", ""),
                "order_index": module_data.get("moduleNumber", 1) - 1,
                "learning_objectives": (
                    module_data.get("learningObjectives", [])
                )
            }
            
            module = await syllabus_service.create_module(
                session, certification.id, module_info
            )
            
            # Create topics for this module
            topics = module_data.get("topics", [])
            topic_count = 0
            
            for i, topic in enumerate(topics):
                # Handle both string and object topics
                if isinstance(topic, str):
                    module_num = module_data.get('moduleNumber', 1)
                    desc = f"Topic {i + 1} from Module {module_num}"
                    topic_data = {
                        "title": topic,
                        "description": desc,
                        "introduction": "",
                        "order_index": i,
                        "estimated_duration": "15 minutes"
                    }
                elif isinstance(topic, dict):
                    topic_data = {
                        "title": topic.get("title", f"Topic {i + 1}"),
                        "description": topic.get("title", f"Topic {i + 1}"),
                        "introduction": "",
                        "order_index": i,
                        "estimated_duration": "15 minutes"
                    }
                    
                    # If topic has detailed content, extract introduction
                    has_content = (
                        "content" in topic and
                        isinstance(topic["content"], dict)
                    )
                    if has_content:
                        topic_data["introduction"] = (
                            topic["content"].get("introduction", "")
                        )
                else:
                    continue  # Skip invalid topic format
                
                await syllabus_service.create_topic(
                    session, module.id, topic_data
                )
                topic_count += 1
            
            mod_num = module_data.get('moduleNumber', '?')
            mod_title = module_info['title']
            print(
                f"✅ Created Module {mod_num}: {mod_title} with "
                f"{topic_count} topics"
            )
        
    except Exception as e:
        print(f"❌ Error creating syllabus: {e}")
        import traceback
        traceback.print_exc()


async def populate_frontend_detailed_content(session):
    """Populate detailed content for Frontend React Fundamentals topics"""
    print("📚 Populating detailed content for Frontend topics...")
    
    try:
        # Import the detailed content from our files
        topics_path = os.path.join(
            os.path.dirname(__file__), "..", "syllabus", "frontend",
            "fundamentals", "topics"
        )
        
        if os.path.exists(topics_path):
            try:
                # Use importlib to dynamically import modules
                from importlib.util import (
                    spec_from_file_location, module_from_spec
                )
                
                modules_dict = {}
                
                # Load Module 1 topics
                module1_path = os.path.join(topics_path, "module1")
                for topic_name in MODULE1_TOPICS:
                    topic_file = os.path.join(
                        module1_path, f"{topic_name}.py"
                    )
                    if os.path.exists(topic_file):
                        spec = spec_from_file_location(
                            topic_name, topic_file
                        )
                        if spec and spec.loader:
                            module = module_from_spec(spec)
                            spec.loader.exec_module(module)
                            modules_dict[topic_name] = module
                
                # Load Module 2 topics
                module2_path = os.path.join(topics_path, "module2")
                for topic_name in MODULE2_TOPICS:
                    topic_file = os.path.join(
                        module2_path, f"{topic_name}.py"
                    )
                    if os.path.exists(topic_file):
                        spec = spec_from_file_location(
                            topic_name, topic_file
                        )
                        if spec and spec.loader:
                            module = module_from_spec(spec)
                            spec.loader.exec_module(module)
                            modules_dict[topic_name] = module
                
                content_map = {}
                
                for module_name, topic_title in TOPIC_MAPPING.items():
                    if module_name in modules_dict:
                        mod_dict = modules_dict[module_name]
                        content_map[topic_title] = mod_dict.TOPIC_CONTENT
                
                # Get frontend react fundamentals certification
                stmt = select(Certification).options(
                    selectinload(Certification.syllabus_modules).options(
                        selectinload(SyllabusModule.topics)
                    )
                ).where(
                    Certification.slug == "frontend-react-fundamentals"
                )
                result = await session.execute(stmt)
                certification = result.scalar_one_or_none()
                
                if certification:
                    updated_count = 0
                    
                    # Update topics with detailed content
                    for module in certification.syllabus_modules:
                        for topic in module.topics:
                            if topic.title in content_map:
                                detailed_content = content_map[topic.title]
                                
                                # Convert the content to JSON string
                                topic.detailed_content = json.dumps(
                                    detailed_content, indent=2
                                )
                                
                                updated_count += 1
                    
                    print(
                        f"✅ Updated {updated_count} topics with "
                        f"detailed content"
                    )
                else:
                    print(
                        "⚠️  Frontend React Fundamentals "
                        "certification not found"
                    )
                    
            except Exception as e:
                print(f"⚠️  Could not import detailed content files: {e}")
        else:
            print("⚠️  Detailed content directory not found")
            
    except Exception as e:
        print(f"❌ Error populating frontend detailed content: {e}")


async def populate_detailed_content(session):
    """Populate detailed content for syllabus topics"""
    print("📚 Populating detailed content for topics...")
    
    try:
        # Import the detailed content from our files
        topics_path = os.path.join(
            os.path.dirname(__file__), "..", "seed_data", "certifications",
            "information_technology", "system_design", "syllabus",
            "fundamentals", "topics"
        )
        
        if os.path.exists(topics_path):
            try:
                # Use importlib to dynamically import modules
                from importlib.util import (
                    spec_from_file_location, module_from_spec
                )
                
                modules_dict = {}
                module_names = [
                    "what_is_system_design",
                    "why_system_design_matters",
                    "common_architecture_patterns",
                    "scalability_fundamentals"
                ]
                
                for module_name in module_names:
                    module_file = os.path.join(
                        topics_path, f"{module_name}.py"
                    )
                    if os.path.exists(module_file):
                        spec = spec_from_file_location(
                            module_name, module_file
                        )
                        if spec and spec.loader:
                            module = module_from_spec(spec)
                            spec.loader.exec_module(module)
                            modules_dict[module_name] = module
                
                content_map = {}
                if "what_is_system_design" in modules_dict:
                    mod_dict = modules_dict["what_is_system_design"]
                    content_map["What is System Design?"] = (
                        mod_dict.TOPIC_CONTENT
                    )
                if "why_system_design_matters" in modules_dict:
                    mod_dict = modules_dict["why_system_design_matters"]
                    content_map["Why System Design Matters"] = (
                        mod_dict.TOPIC_CONTENT
                    )
                if "common_architecture_patterns" in modules_dict:
                    mod_dict = modules_dict["common_architecture_patterns"]
                    content_map["Common Architecture Patterns"] = (
                        mod_dict.TOPIC_CONTENT
                    )
                if "scalability_fundamentals" in modules_dict:
                    mod_dict = modules_dict["scalability_fundamentals"]
                    content_map["Scalability Fundamentals"] = (
                        mod_dict.TOPIC_CONTENT
                    )
                
                # Get system design certification
                stmt = select(Certification).options(
                    selectinload(Certification.syllabus_modules).options(
                        selectinload(SyllabusModule.topics)
                    )
                ).where(
                    Certification.slug == "system-design-fundamentals"
                )
                result = await session.execute(stmt)
                certification = result.scalar_one_or_none()
                
                if certification:
                    updated_count = 0
                    
                    # Update topics with detailed content
                    for module in certification.syllabus_modules:
                        for topic in module.topics:
                            if topic.title in content_map:
                                detailed_content = content_map[topic.title]
                                
                                # Convert the content to JSON string
                                topic.detailed_content = json.dumps(
                                    detailed_content, indent=2
                                )
                                
                                updated_count += 1
                    
                    print(
                        f"✅ Updated {updated_count} topics with "
                        f"detailed content"
                    )
                else:
                    print(
                        "⚠️  System Design Fundamentals "
                        "certification not found"
                    )
                    
            except Exception as e:
                print(f"⚠️  Could not import detailed content files: {e}")
        else:
            print("⚠️  Detailed content directory not found")
            
    except Exception as e:
        print(f"❌ Error populating detailed content: {e}")
