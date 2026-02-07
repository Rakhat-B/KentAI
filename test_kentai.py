"""
Tests for KentAI automation engine
"""
import unittest
from kentai.automation import AutomationEngine


class TestAutomationEngine(unittest.TestCase):
    """Test automation functionality"""
    
    def setUp(self):
        """Set up test engine"""
        self.engine = AutomationEngine()
    
    def test_lazy_mode_execution(self):
        """Test lazy mode action execution"""
        result = self.engine.execute_action({'action': 'lazy_mode', 'value': True})
        self.assertEqual(result['status'], 'success')
        self.assertIn('results', result)
        self.assertIn('steam', result['results'])
        self.assertIn('discord', result['results'])
        self.assertIn('youtube', result['results'])
    
    def test_work_mode_execution(self):
        """Test work mode action execution"""
        result = self.engine.execute_action({'action': 'work_mode', 'value': True})
        self.assertEqual(result['status'], 'success')
        self.assertIn('results', result)
        self.assertIn('vscode', result['results'])
        self.assertIn('notion', result['results'])
        self.assertIn('gmail', result['results'])
    
    def test_open_apps_execution(self):
        """Test opening multiple apps"""
        result = self.engine.execute_action({
            'action': 'open_apps',
            'value': ['youtube', 'gmail']
        })
        self.assertEqual(result['status'], 'success')
        self.assertIn('youtube', result['results'])
        self.assertIn('gmail', result['results'])
    
    def test_unknown_action(self):
        """Test unknown action handling"""
        result = self.engine.execute_action({
            'action': 'unknown_action',
            'value': True
        })
        self.assertEqual(result['status'], 'unknown_action')
    
    def test_no_action(self):
        """Test no action provided"""
        result = self.engine.execute_action(None)
        self.assertEqual(result['status'], 'no_action')


class TestBrain(unittest.TestCase):
    """Test KentAI brain functionality"""
    
    def test_action_extraction(self):
        """Test JSON action extraction from message"""
        from kentai.brain import KentAIBrain
        
        brain = KentAIBrain()
        
        # Test with JSON block
        message = '''Yo dude!
```json
{"action": "lazy_mode", "value": true}
```'''
        action = brain._extract_action(message)
        self.assertIsNotNone(action)
        self.assertEqual(action['action'], 'lazy_mode')
        self.assertEqual(action['value'], True)
    
    def test_response_cleaning(self):
        """Test cleaning JSON from response"""
        from kentai.brain import KentAIBrain
        
        brain = KentAIBrain()
        
        message = '''Let's do it!
```json
{"action": "work_mode"}
```'''
        clean = brain._clean_response(message)
        self.assertEqual(clean, "Let's do it!")
        self.assertNotIn('```', clean)


if __name__ == '__main__':
    unittest.main()
