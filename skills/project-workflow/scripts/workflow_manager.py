#!/usr/bin/env python3
"""
Workflow Manager - Manage project workflow and orchestrate skill execution.

Usage:
    python workflow_manager.py init <scenario> <name>     Initialize new workflow
    python workflow_manager.py status [name]              Show workflow status
    python workflow_manager.py next <name>                Advance to next stage
    python workflow_manager.py goto <name> <stage-id>     Jump to specified stage
    python workflow_manager.py report                     Generate progress report
    python workflow_manager.py list                       List all active workflows
    python workflow_manager.py archive <name>             Archive completed workflow
"""

import sys
import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any


class WorkflowManager:
    """Manage project workflows stored in YAML format."""
    
    VALID_SCENARIOS = ["project_init", "feature_dev", "bug_fix", "docs_update"]
    VALID_STATUSES = ["active", "completed", "archived"]
    
    # Define workflow stages for each scenario
    SCENARIO_STAGES = {
        "project_init": [
            {"name": "project-structure", "skill": "project-structure"},
            {"name": "brainstorming", "skill": "brainstorming"},
            {"name": "project-docs", "skill": "project-docs"},
            {"name": "writing-plans", "skill": "writing-plans"},
            {"name": "project-task", "skill": "project-task"},
        ],
        "feature_dev": [
            {"name": "brainstorming", "skill": "brainstorming"},
            {"name": "project-docs", "skill": "project-docs"},
            {"name": "writing-plans", "skill": "writing-plans"},
            {"name": "project-task", "skill": "project-task"},
            {"name": "executing-plans", "skill": "executing-plans"},
            {"name": "requesting-code-review", "skill": "requesting-code-review"},
            {"name": "finishing-a-development-branch", "skill": "finishing-a-development-branch"},
        ],
        "bug_fix": [
            {"name": "systematic-debugging", "skill": "systematic-debugging"},
            {"name": "project-task", "skill": "project-task"},
            {"name": "executing-plans", "skill": "executing-plans"},
            {"name": "verification-before-completion", "skill": "verification-before-completion"},
        ],
        "docs_update": [
            {"name": "project-docs", "skill": "project-docs"},
            {"name": "project-task", "skill": "project-task"},
        ],
    }
    
    def __init__(self, workflow_dir: str = "docs/workflow"):
        self.workflow_dir = Path(workflow_dir)
        
    def init_workflow(self, scenario: str, name: str) -> Path:
        """Initialize a new workflow."""
        if scenario not in self.VALID_SCENARIOS:
            print(f"Error: Invalid scenario '{scenario}'")
            print(f"Valid scenarios: {', '.join(self.VALID_SCENARIOS)}")
            sys.exit(1)
        
        self.workflow_dir.mkdir(parents=True, exist_ok=True)
        
        workflow_file = self.workflow_dir / f"{name}.yaml"
        if workflow_file.exists():
            print(f"Error: Workflow '{name}' already exists")
            sys.exit(1)
        
        now = datetime.now().isoformat()
        stages = self.SCENARIO_STAGES[scenario]
        
        stage_data = []
        for i, stage in enumerate(stages, 1):
            stage_data.append({
                "id": i,
                "name": stage["name"],
                "skill": stage["skill"],
                "status": "pending",
                "started_at": None,
                "completed_at": None,
                "output": None,
            })
        
        workflow_data = {
            "scenario": scenario,
            "project_name": name,
            "created": now,
            "updated": now,
            "current_stage": 1,
            "status": "active",
            "stages": stage_data,
        }
        
        with open(workflow_file, 'w') as f:
            yaml.dump(workflow_data, f, default_flow_style=False, sort_keys=False)
        
        print(f"Initialized workflow: {workflow_file}")
        print(f"Scenario: {scenario}")
        print(f"Stages: {len(stages)}")
        for stage in stage_data:
            print(f"  {stage['id']}. {stage['name']} ({stage['skill']})")
        
        return workflow_file
    
    def load_workflow(self, name: str) -> Dict[str, Any]:
        """Load workflow from YAML file."""
        workflow_file = self.workflow_dir / f"{name}.yaml"
        if not workflow_file.exists():
            print(f"Error: Workflow '{name}' not found")
            sys.exit(1)
        
        with open(workflow_file, 'r') as f:
            return yaml.safe_load(f)
    
    def save_workflow(self, name: str, data: Dict[str, Any]) -> None:
        """Save workflow to YAML file."""
        data["updated"] = datetime.now().isoformat()
        workflow_file = self.workflow_dir / f"{name}.yaml"
        with open(workflow_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    def status(self, name: str) -> None:
        """Show workflow status."""
        data = self.load_workflow(name)
        self.print_status(data)
    
    def print_status(self, data: Dict[str, Any]) -> None:
        """Print workflow status."""
        print(f"\n=== Workflow: {data['project_name']} ===")
        print(f"Scenario: {data['scenario']}")
        print(f"Status: {data['status']}")
        print(f"Current Stage: {data['current_stage']}/{len(data['stages'])}")
        print()
        
        stages = data["stages"]
        current = data["current_stage"]
        
        print(f"{'ID':<4} {'Status':<12} {'Stage':<25} {'Skill':<30}")
        print("-" * 75)
        
        for stage in stages:
            status = stage["status"]
            name = stage["name"][:23] + ".." if len(stage["name"]) > 25 else stage["name"]
            skill = stage["skill"][:28] + ".." if len(stage["skill"]) > 30 else stage["skill"]
            marker = " →" if stage["id"] == current else "  "
            print(f"{marker}{stage['id']:<3} {status:<12} {name:<25} {skill:<30}")
        
        print()
        completed = sum(1 for s in stages if s["status"] == "completed")
        total = len(stages)
        percent = (completed / total * 100) if total > 0 else 0
        print(f"Progress: {completed}/{total} ({percent:.1f}%)")
    
    def next_stage(self, name: str) -> None:
        """Advance to the next stage."""
        data = self.load_workflow(name)
        
        if data["status"] != "active":
            print(f"Workflow '{name}' is not active")
            return
        
        current_idx = data["current_stage"] - 1
        stages = data["stages"]
        
        if current_idx >= len(stages):
            print("All stages completed!")
            return
        
        # Mark current stage as completed
        current_stage = stages[current_idx]
        if current_stage["status"] == "pending":
            current_stage["status"] = "completed"
            current_stage["completed_at"] = datetime.now().isoformat()
        
        # Check if there's a next stage
        if current_idx + 1 < len(stages):
            next_stage = stages[current_idx + 1]
            next_stage["status"] = "in_progress"
            next_stage["started_at"] = datetime.now().isoformat()
            
            data["current_stage"] = current_idx + 2
            
            print(f"\nAdvancing to stage {data['current_stage']}: {next_stage['name']}")
            print(f"Triggering skill: {next_stage['skill']}")
            
            # In real implementation, this would trigger the skill
            # For now, we just update the state
            print(f"[Skill execution would happen here: {next_stage['skill']}]")
        else:
            # All stages completed
            data["status"] = "completed"
            current_stage["completed_at"] = datetime.now().isoformat()
            print("\n=== All stages completed! ===")
        
        self.save_workflow(name, data)
        self.print_status(data)
    
    def goto_stage(self, name: str, stage_id: int) -> None:
        """Jump to a specific stage."""
        data = self.load_workflow(name)
        stages = data["stages"]
        
        if stage_id < 1 or stage_id > len(stages):
            print(f"Error: Invalid stage ID {stage_id}")
            print(f"Valid range: 1-{len(stages)}")
            return
        
        # Update all stages before target to completed
        for i, stage in enumerate(stages):
            if stage["id"] < stage_id:
                stage["status"] = "completed"
                if not stage["completed_at"]:
                    stage["completed_at"] = datetime.now().isoformat()
            elif stage["id"] == stage_id:
                stage["status"] = "in_progress"
                if not stage["started_at"]:
                    stage["started_at"] = datetime.now().isoformat()
            else:
                stage["status"] = "pending"
                stage["started_at"] = None
                stage["completed_at"] = None
        
        data["current_stage"] = stage_id
        self.save_workflow(name, data)
        
        print(f"Jumped to stage {stage_id}: {stages[stage_id - 1]['name']}")
        self.print_status(data)
    
    def generate_report(self) -> None:
        """Generate progress report for all workflows."""
        workflow_files = list(self.workflow_dir.glob("*.yaml"))
        
        if not workflow_files:
            print("No workflows found")
            return
        
        print("\n=== Workflow Progress Report ===\n")
        
        total_workflows = len(workflow_files)
        completed_workflows = 0
        total_stages = 0
        completed_stages = 0
        
        for wf in sorted(workflow_files):
            with open(wf, 'r') as f:
                data = yaml.safe_load(f)
            
            stages = data["stages"]
            completed = sum(1 for s in stages if s["status"] == "completed")
            total = len(stages)
            percent = (completed / total * 100) if total > 0 else 0
            
            total_stages += total
            completed_stages += completed
            
            if data["status"] == "completed":
                completed_workflows += 1
            
            status_icon = "✓" if data["status"] == "completed" else "○"
            current = f"{data['current_stage']}/{total}"
            print(f"{status_icon} {data['project_name']:<25} {data['scenario']:<15} Stage: {current} ({percent:.0f}%)")
        
        print()
        overall_workflow = (completed_workflows / total_workflows * 100) if total_workflows > 0 else 0
        overall_stages = (completed_stages / total_stages * 100) if total_stages > 0 else 0
        print(f"Summary: {completed_workflows}/{total_workflows} workflows complete ({overall_workflow:.0f}%)")
        print(f"         {completed_stages}/{total_stages} stages complete ({overall_stages:.0f}%)")
    
    def list_workflows(self) -> None:
        """List all active workflows."""
        workflow_files = list(self.workflow_dir.glob("*.yaml"))
        
        if not workflow_files:
            print("No workflows found")
            return
        
        print("\n=== Active Workflows ===\n")
        
        active_count = 0
        for wf in sorted(workflow_files):
            with open(wf, 'r') as f:
                data = yaml.safe_load(f)
            
            if data["status"] == "active":
                active_count += 1
                current_stage = data["stages"][data["current_stage"] - 1]
                print(f"• {data['project_name']}")
                print(f"  Scenario: {data['scenario']}")
                print(f"  Current:  Stage {data['current_stage']}: {current_stage['name']}")
                print()
        
        if active_count == 0:
            print("No active workflows")
    
    def archive_workflow(self, name: str) -> None:
        """Archive a completed workflow."""
        data = self.load_workflow(name)
        
        if data["status"] != "completed":
            print(f"Warning: Workflow '{name}' is not marked as completed")
            confirm = input("Archive anyway? (y/N): ")
            if confirm.lower() != 'y':
                print("Archive cancelled")
                return
        
        data["status"] = "archived"
        self.save_workflow(name, data)
        print(f"Archived workflow: {name}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    manager = WorkflowManager()
    command = sys.argv[1]
    
    if command == "init":
        if len(sys.argv) < 4:
            print("Usage: python workflow_manager.py init <scenario> <name>")
            print(f"Scenarios: {', '.join(manager.VALID_SCENARIOS)}")
            sys.exit(1)
        scenario = sys.argv[2]
        name = sys.argv[3]
        manager.init_workflow(scenario, name)
    
    elif command == "status":
        if len(sys.argv) < 3:
            print("Usage: python workflow_manager.py status <name>")
            sys.exit(1)
        manager.status(sys.argv[2])
    
    elif command == "next":
        if len(sys.argv) < 3:
            print("Usage: python workflow_manager.py next <name>")
            sys.exit(1)
        manager.next_stage(sys.argv[2])
    
    elif command == "goto":
        if len(sys.argv) < 4:
            print("Usage: python workflow_manager.py goto <name> <stage-id>")
            sys.exit(1)
        name = sys.argv[2]
        stage_id = int(sys.argv[3])
        manager.goto_stage(name, stage_id)
    
    elif command == "report":
        manager.generate_report()
    
    elif command == "list":
        manager.list_workflows()
    
    elif command == "archive":
        if len(sys.argv) < 3:
            print("Usage: python workflow_manager.py archive <name>")
            sys.exit(1)
        manager.archive_workflow(sys.argv[2])
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
