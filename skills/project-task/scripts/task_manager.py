#!/usr/bin/env python3
"""
Task Manager - Manage and execute task lists automatically.

Usage:
    python task_manager.py create <name>              Create new task list
    python task_manager.py add <file> <task>          Add task to list
    python task_manager.py run <file>                 Execute tasks automatically
    python task_manager.py status <file>              Show task status
    python task_manager.py report                     Generate progress report
    python task_manager.py convert <plan-file>        Convert plan to tasks
"""

import sys
import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any


class TaskManager:
    """Manage task lists stored in YAML format."""
    
    VALID_STATUSES = ["pending", "in_progress", "completed", "blocked"]
    VALID_PRIORITIES = ["low", "medium", "high"]
    
    def __init__(self, tasks_dir: str = "docs/task"):
        self.tasks_dir = Path(tasks_dir)
        
    def create_task_list(self, name: str, description: str = "") -> Path:
        """Create a new task list file."""
        self.tasks_dir.mkdir(parents=True, exist_ok=True)
        
        task_file = self.tasks_dir / f"{name}.yaml"
        if task_file.exists():
            print(f"Error: Task list '{name}' already exists")
            sys.exit(1)
        
        now = datetime.now().isoformat()
        task_data = {
            "name": name,
            "description": description,
            "created": now,
            "updated": now,
            "tasks": []
        }
        
        with open(task_file, 'w') as f:
            yaml.dump(task_data, f, default_flow_style=False, sort_keys=False)
        
        print(f"Created task list: {task_file}")
        return task_file
    
    def load_tasks(self, file_path: str) -> Dict[str, Any]:
        """Load tasks from YAML file."""
        path = Path(file_path)
        if not path.exists():
            print(f"Error: Task file '{file_path}' not found")
            sys.exit(1)
        
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def save_tasks(self, file_path: str, data: Dict[str, Any]) -> None:
        """Save tasks to YAML file."""
        data["updated"] = datetime.now().isoformat()
        with open(Path(file_path), 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    def add_task(self, file_path: str, name: str, description: str = "",
                 priority: str = "medium", dependencies: List[int] = None) -> None:
        """Add a task to the list."""
        data = self.load_tasks(file_path)
        
        # Get next ID
        next_id = 1
        if data["tasks"]:
            next_id = max(t["id"] for t in data["tasks"]) + 1
        
        now = datetime.now().isoformat()
        task = {
            "id": next_id,
            "name": name,
            "description": description,
            "status": "pending",
            "priority": priority,
            "created": now,
            "started": None,
            "completed": None,
            "dependencies": dependencies or [],
            "notes": []
        }
        
        data["tasks"].append(task)
        self.save_tasks(file_path, data)
        print(f"Added task #{next_id}: {name}")
    
    def get_next_task(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Get the next executable task (no blocked dependencies)."""
        tasks = data["tasks"]
        
        # Find pending tasks with all dependencies completed
        for task in sorted(tasks, key=lambda t: (t["priority"] != "high", t["id"])):
            if task["status"] != "pending":
                continue
            
            # Check dependencies
            deps_completed = True
            for dep_id in task.get("dependencies", []):
                dep_task = next((t for t in tasks if t["id"] == dep_id), None)
                if not dep_task or dep_task["status"] != "completed":
                    deps_completed = False
                    break
            
            if deps_completed:
                return task
        
        return None
    
    def start_task(self, file_path: str, task_id: int) -> None:
        """Mark a task as in_progress."""
        data = self.load_tasks(file_path)
        
        for task in data["tasks"]:
            if task["id"] == task_id:
                task["status"] = "in_progress"
                task["started"] = datetime.now().isoformat()
                break
        
        self.save_tasks(file_path, data)
        print(f"Started task #{task_id}")
    
    def complete_task(self, file_path: str, task_id: int, notes: str = "") -> None:
        """Mark a task as completed."""
        data = self.load_tasks(file_path)
        
        for task in data["tasks"]:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed"] = datetime.now().isoformat()
                if notes:
                    task["notes"].append(notes)
                break
        
        self.save_tasks(file_path, data)
        print(f"Completed task #{task_id}")
    
    def run_tasks(self, file_path: str, dry_run: bool = False) -> None:
        """Execute tasks automatically in order."""
        data = self.load_tasks(file_path)
        
        if not data["tasks"]:
            print("No tasks to execute")
            return
        
        print(f"\n=== Executing tasks from {file_path} ===\n")
        
        completed_count = sum(1 for t in data["tasks"] if t["status"] == "completed")
        total_count = len(data["tasks"])
        
        while True:
            next_task = self.get_next_task(data)
            
            if not next_task:
                # Check if all tasks are done
                remaining = [t for t in data["tasks"] if t["status"] != "completed"]
                if not remaining:
                    print("\n=== All tasks completed! ===\n")
                else:
                    print(f"\n=== Blocked: {len(remaining)} tasks have unmet dependencies ===\n")
                    for t in remaining:
                        print(f"  #{t['id']}: {t['name']} (waiting on: {t.get('dependencies', [])})")
                break
            
            print(f"Executing task #{next_task['id']}: {next_task['name']}")
            
            if dry_run:
                print(f"  [DRY RUN] Would execute: {next_task['description']}")
            else:
                # In real execution, this would trigger subagents or commands
                # For now, we just mark status and simulate execution
                print(f"  Description: {next_task['description']}")
                
                # Start the task
                self.start_task(file_path, next_task["id"])
                
                # Simulate task execution (in real use, this would do actual work)
                # For demo purposes, we auto-complete after "execution"
                print(f"  Status: Executing...")
                
                # Complete the task
                self.complete_task(file_path, next_task["id"])
                print(f"  ✓ Completed\n")
                
                # Reload for next iteration
                data = self.load_tasks(file_path)
        
        # Print summary
        self.print_status(data)
    
    def print_status(self, data: Dict[str, Any]) -> None:
        """Print task status summary."""
        tasks = data["tasks"]
        
        print(f"\n=== Task Status: {data['name']} ===\n")
        print(f"{'ID':<4} {'Status':<12} {'Priority':<8} {'Name':<30}")
        print("-" * 60)
        
        for task in sorted(tasks, key=lambda t: t["id"]):
            status = task["status"]
            priority = task["priority"]
            name = task["name"][:28] + ".." if len(task["name"]) > 30 else task["name"]
            print(f"{task['id']:<4} {status:<12} {priority:<8} {name}")
        
        print()
        completed = sum(1 for t in tasks if t["status"] == "completed")
        total = len(tasks)
        percent = (completed / total * 100) if total > 0 else 0
        print(f"Progress: {completed}/{total} ({percent:.1f}%)")
    
    def generate_report(self) -> None:
        """Generate progress report for all task lists."""
        task_files = list(self.tasks_dir.glob("*.yaml"))
        
        if not task_files:
            print("No task lists found")
            return
        
        print("\n=== Task Progress Report ===\n")
        
        total_tasks = 0
        total_completed = 0
        
        for tf in sorted(task_files):
            data = self.load_tasks(str(tf))
            tasks = data["tasks"]
            completed = sum(1 for t in tasks if t["status"] == "completed")
            total = len(tasks)
            percent = (completed / total * 100) if total > 0 else 0
            
            total_tasks += total
            total_completed += completed
            
            status_str = f"{completed}/{total} ({percent:.1f}%)"
            print(f"{data['name']:<20} {status_str}")
        
        print()
        overall = (total_completed / total_tasks * 100) if total_tasks > 0 else 0
        print(f"Overall: {total_completed}/{total_tasks} ({overall:.1f}%)")
    
    def convert_plan_to_tasks(self, plan_file: str, task_name: str = None) -> None:
        """Convert a plan file to task list."""
        plan_path = Path(plan_file)
        if not plan_path.exists():
            print(f"Error: Plan file '{plan_file}' not found")
            sys.exit(1)
        
        # Extract task name from plan filename if not provided
        if not task_name:
            task_name = plan_path.stem.split("-", 3)[-1] if "-" in plan_path.stem else "tasks"
        
        # Read plan content
        with open(plan_path, 'r') as f:
            plan_content = f.read()
        
        # Create task list
        self.create_task_list(task_name, f"Tasks from {plan_path.name}")
        task_file = self.tasks_dir / f"{task_name}.yaml"
        
        # Parse plan and extract tasks (simplified - in real use would use LLM)
        # For now, create placeholder tasks
        data = self.load_tasks(str(task_file))
        
        # Add placeholder tasks based on plan sections
        sections = plan_content.split("##")
        prev_id = 0
        
        for section in sections[1:]:  # Skip empty first section
            lines = section.strip().split("\n")
            section_name = lines[0].strip() if lines else "Unknown"
            
            now = datetime.now().isoformat()
            task = {
                "id": prev_id + 1,
                "name": f"Implement: {section_name}",
                "description": f"See {plan_path.name} for details on {section_name}",
                "status": "pending",
                "priority": "medium",
                "created": now,
                "started": None,
                "completed": None,
                "dependencies": [prev_id] if prev_id > 0 else [],
                "notes": []
            }
            
            data["tasks"].append(task)
            prev_id = task["id"]
        
        self.save_tasks(str(task_file), data)
        print(f"Converted plan to {len(data['tasks'])} tasks in {task_file}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    manager = TaskManager()
    command = sys.argv[1]
    
    if command == "create":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py create <name> [description]")
            sys.exit(1)
        name = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        manager.create_task_list(name, description)
    
    elif command == "add":
        if len(sys.argv) < 4:
            print("Usage: python task_manager.py add <file> <task_name> [description]")
            sys.exit(1)
        file_path = sys.argv[2]
        name = sys.argv[3]
        description = sys.argv[4] if len(sys.argv) > 4 else ""
        manager.add_task(file_path, name, description)
    
    elif command == "run":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py run <file> [--dry-run]")
            sys.exit(1)
        file_path = sys.argv[2]
        dry_run = "--dry-run" in sys.argv
        manager.run_tasks(file_path, dry_run)
    
    elif command == "status":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py status <file>")
            sys.exit(1)
        data = manager.load_tasks(sys.argv[2])
        manager.print_status(data)
    
    elif command == "report":
        manager.generate_report()
    
    elif command == "convert":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py convert <plan-file> [task-name]")
            sys.exit(1)
        plan_file = sys.argv[2]
        task_name = sys.argv[3] if len(sys.argv) > 3 else None
        manager.convert_plan_to_tasks(plan_file, task_name)
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
