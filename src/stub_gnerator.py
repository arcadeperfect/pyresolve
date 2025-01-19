import inspect
from typing import Any, Set, Dict
from get_resolve import GetResolve

def get_methods(obj: Any) -> Set[str]:
    methods = set()

    # for name, _ in inspect.getmembers(obj, inspect.ismethod):
    #     if not name.startswith("_"):
    #         methods.add(name)
    methods = set()
    
    for name in dir(obj):
        # Skip private attributes
        if name.startswith('_'):
            continue
            
        try:
            attr = getattr(obj, name)
            # Check if it's callable (a method or function)
            if callable(attr):
                methods.add(name)
        except Exception as e:
            print(f"Warning: Couldn't access {name}: {e}")
    
    return methods

    

def generate_class_stub(class_name: str, methods: Set[str]) -> str:
    stub = f"class {class_name}(PyRemoteObject):\n"
    stub += '    """TODO: Add docstring."""\n\n'

    for method in sorted(methods):
        stub += f"    def {method}(self) -> Any:\n"
        stub += '        """TODO: Add method docstring.\n\n'
        stub += "        Returns:\n"
        stub += "            Any: TODO: Add return docstring.\n"
        stub += '        """\n'
        stub += "        ...\n\n"
    
    return stub

def generate_stubs(resolve) -> None:
    """Generate stubs for all discovered Resolve objects."""
    # Start with basic imports
    stub_content = """from typing import Optional, List, Dict, Any, Protocol, Union

class PyRemoteObject(Protocol):
    \"\"\"Base type for all Resolve objects.\"\"\"
    pass

"""
    
    # Dictionary to store discovered classes and their methods
    classes: Dict[str, Set[str]] = {}
    
    # Get initial Project object
    project_manager = resolve.GetProjectManager()
    project = project_manager.GetCurrentProject()
    
    # Collect methods from common objects
    objects_to_analyze = {
        'Resolve': resolve,
        'ProjectManager': project_manager,
        'Project': project,
        'MediaPool': project.GetMediaPool(),
        'Timeline': project.GetCurrentTimeline(),
        'MediaStorage': resolve.GetMediaStorage()
    }
    
    # Try to get additional objects
    try:
        media_pool = project.GetMediaPool()
        if media_pool:
            folder = media_pool.GetRootFolder()
            if folder:
                objects_to_analyze['Folder'] = folder
                clips = folder.GetClipList()
                if clips and len(clips) > 0:
                    objects_to_analyze['MediaPoolItem'] = clips[0]
        timeline = project.GetCurrentTimeline()
        if timeline:
            objects_to_analyze['TimelineItem'] = project.GetCurrentTimeline().GetCurrentVideoItem()

    except Exception as e:
        print(f"Warning: Couldn't analyze some objects: {e}")
    

    print("\nObjects to analyze:\n")
    for class_name, obj in objects_to_analyze.items():
        if obj is not None:
            print(f"- {class_name}")
    print("\n")

    # Collect methods for each object
    for class_name, obj in objects_to_analyze.items():
        print(f"Collecting methods for {class_name}")
        if obj is not None:
            classes[class_name] = get_methods(obj)
            print("\tfound methods:")
            for method in classes[class_name]:
                print(f"\t- {method}")
            print("\n")
    
    # Generate stub content
    for class_name, methods in sorted(classes.items()):
        stub_content += generate_class_stub(class_name, methods) + "\n"
    
    # Write to file
    with open('__resolve.pyi', 'w') as f:
        f.write(stub_content)


def main():
    # Initialize Resolve
    try:
        # Your Resolve initialization code here
        resolve = GetResolve()
        generate_stubs(resolve)
        print("Stubs generated successfully!")
    except Exception as e:
        print(f"Error generating stubs: {e}")

if __name__ == '__main__':
    main()