#!/usr/bin/env python3
"""
Batch File Renamer
A flexible script to rename multiple files in a folder based on various patterns.
Supported patterns:
- Sequential numbering
- Date-based naming
- Custom prefix
- Original name with prefix/suffix
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import argparse


class FileRenamer:
    def __init__(self, target_folder, pattern_type, **kwargs):
        """
        Initialize the FileRenamer.
        
        Args:
            target_folder: Path to the folder containing files to rename
            pattern_type: Type of naming pattern to use
            **kwargs: Additional parameters for specific patterns
        """
        self.target_folder = Path(target_folder)
        self.pattern_type = pattern_type
        self.options = kwargs

        if not self.target_folder.exists():
            raise FileNotFoundError(f"Folder not found: {target_folder}")
        if not self.target_folder.is_dir():
            raise NotADirectoryError(f"Not a directory: {target_folder}")

    def get_files(self, file_extension=None):
        """
        Get list of files in the target folder.
        
        Args:
            file_extension: Filter by extension (e.g., '.txt', '.jpg')
        
        Returns:
            List of Path objects
        """
        files = [f for f in self.target_folder.iterdir() if f.is_file()]

        if file_extension:
            files = [f for f in files if f.suffix.lower() == file_extension.lower()]

        return sorted(files)

    def generate_new_name(self, old_file, index, total_files):
        """
        Generate new filename based on the selected pattern.
        
        Args:
            old_file: Path object of the original file
            index: Current file index
            total_files: Total number of files being renamed
        
        Returns:
            New filename string
        """
        extension = old_file.suffix

        if self.pattern_type == 'sequential':
            # Sequential numbering: file_001.txt, file_002.txt, etc.
            prefix = self.options.get('prefix', 'file')
            padding = len(str(total_files))
            new_name = f"{prefix}_{str(index).zfill(padding)}{extension}"

        elif self.pattern_type == 'date':
            # Date-based: 2025-10-21_001.txt
            date_format = self.options.get('date_format', '%Y-%m-%d')
            date_str = datetime.now().strftime(date_format)
            padding = len(str(total_files))
            new_name = f"{date_str}_{str(index).zfill(padding)}{extension}"

        elif self.pattern_type == 'custom':
            # Custom pattern with placeholders
            template = self.options.get('template', '{prefix}_{index}{ext}')
            padding = self.options.get('padding', 3)
            new_name = template.format(
                prefix=self.options.get('prefix', 'file'),
                index=str(index).zfill(padding),
                original=old_file.stem,
                ext=extension,
                date=datetime.now().strftime('%Y%m%d'),
                time=datetime.now().strftime('%H%M%S')
            )

        elif self.pattern_type == 'prefix':
            # Add prefix to original name: PREFIX_originalname.txt
            prefix = self.options.get('prefix', 'new')
            new_name = f"{prefix}_{old_file.name}"

        elif self.pattern_type == 'suffix':
            # Add suffix to original name: originalname_SUFFIX.txt
            suffix = self.options.get('suffix', 'modified')
            new_name = f"{old_file.stem}_{suffix}{extension}"

        else:
            raise ValueError(f"Unknown pattern type: {self.pattern_type}")

        return new_name

    def preview_changes(self, file_extension=None):
        """
        Preview the renaming changes without applying them.
        
        Args:
            file_extension: Filter by extension
        
        Returns:
            List of tuples (old_name, new_name)
        """
        files = self.get_files(file_extension)
        changes = []

        for index, file in enumerate(files, start=1):
            new_name = self.generate_new_name(file, index, len(files))
            changes.append((file.name, new_name))

        return changes

    def rename_files(self, file_extension=None, dry_run=False):
        """
        Rename files in the target folder.
        
        Args:
            file_extension: Filter by extension
            dry_run: If True, only preview changes without renaming
        
        Returns:
            List of tuples (old_path, new_path, success)
        """
        files = self.get_files(file_extension)
        results = []

        for index, file in enumerate(files, start=1):
            new_name = self.generate_new_name(file, index, len(files))
            new_path = self.target_folder / new_name

            # Check for name conflicts
            if new_path.exists() and new_path != file:
                results.append((file, new_path, False, "File already exists"))
                continue

            if not dry_run:
                try:
                    file.rename(new_path)
                    results.append((file, new_path, True, "Success"))
                except Exception as e:
                    results.append((file, new_path, False, str(e)))
            else:
                results.append((file, new_path, True, "Dry run"))

        return results


def main():
    parser = argparse.ArgumentParser(
        description="Batch rename files in a folder with various patterns",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Sequential numbering:
    python file_renamer.py /path/to/folder -p sequential --prefix photo
  
  Date-based naming:
    python file_renamer.py /path/to/folder -p date --date-format "%%Y-%%m-%%d"
  
  Custom template:
    python file_renamer.py /path/to/folder -p custom --template "img_{date}_{index}{ext}"
  
  Add prefix:
    python file_renamer.py /path/to/folder -p prefix --prefix "backup"
  
  Filter by extension:
    python file_renamer.py /path/to/folder -p sequential --ext .jpg
        """
    )

    parser.add_argument('folder', help='Target folder containing files to rename')
    parser.add_argument('-p', '--pattern', required=True,
                       choices=['sequential', 'date', 'custom', 'prefix', 'suffix'],
                       help='Naming pattern to use')
    parser.add_argument('--prefix', default='file', help='Prefix for filename')
    parser.add_argument('--suffix', default='modified', help='Suffix for filename')
    parser.add_argument('--template', help='Custom template (use {prefix}, {index}, {original}, {ext}, {date}, {time})')
    parser.add_argument('--date-format', default='%%Y-%%m-%%d', help='Date format for date pattern')
    parser.add_argument('--padding', type=int, default=3, help='Number of digits for padding')
    parser.add_argument('--ext', help='Filter by file extension (e.g., .txt, .jpg)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without renaming')

    args = parser.parse_args()

    try:
        # Create renamer instance
        renamer = FileRenamer(
            args.folder,
            args.pattern,
            prefix=args.prefix,
            suffix=args.suffix,
            template=args.template,
            date_format=args.date_format,
            padding=args.padding
        )

        # Preview changes
        print(f"\n{'='*70}")
        print(f"Target Folder: {args.folder}")
        print(f"Pattern: {args.pattern}")
        if args.ext:
            print(f"Filter: {args.ext}")
        print(f"{'='*70}\n")

        changes = renamer.preview_changes(args.ext)

        if not changes:
            print("No files found to rename.")
            return

        print("Preview of changes:")
        print(f"{'OLD NAME':<40} -> {'NEW NAME':<40}")
        print("-" * 85)
        for old, new in changes:
            print(f"{old:<40} -> {new:<40}")

        print(f"\nTotal files: {len(changes)}")

        if args.dry_run:
            print("\n[DRY RUN] No files were renamed.")
            return

        # Ask for confirmation
        response = input("\nProceed with renaming? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("Operation cancelled.")
            return

        # Perform renaming
        results = renamer.rename_files(args.ext, dry_run=False)

        # Display results
        print(f"\n{'='*70}")
        print("Results:")
        print(f"{'='*70}\n")

        success_count = 0
        for old, new, success, message in results:
            status = "✓" if success else "✗"
            print(f"{status} {old.name} -> {new.name}")
            if not success:
                print(f"  Error: {message}")
            else:
                success_count += 1

        print(f"\nSuccessfully renamed {success_count}/{len(results)} files.")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
