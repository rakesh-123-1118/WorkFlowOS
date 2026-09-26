import { useEffect, useState } from 'react';

const API_BASE_URL = 'http://localhost:8000/api/v1';

type Workflow = {
  workflow_id?: string;
  name: string;
  description: string;
  intent: string;
  status?: string;
};

type Pattern = {
  name: string;
  confidence: number;
  description: string;
  sources: string[];
  status: string;
};

export default function App() {
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [patterns, setPatterns] = useState<Pattern[]>([]);
  const [loading, setLoading] = useState(true);

  const loadData = async () => {
    try {
      setLoading(true);
      const [workflowResponse, patternResponse] = await Promise.all([
        fetch(`${API_BASE_URL}/workflows`),
        fetch(`${API_BASE_URL}/insights/patterns`),
      ]);

      const workflowData = workflowResponse.ok ? await workflowResponse.json() : [];
      const patternData = patternResponse.ok ? await patternResponse.json() : [];

      setWorkflows(workflowData);
      setPatterns(patternData);
    } catch (error) {
      console.error('Failed to load WorkFlowOS data:', error);
      setWorkflows([]);
      setPatterns([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const discoverWorkflow = async () => {
    const workflowPayload = {
      name: 'Customer Request Processing',
      description: 'Read the email, update the CRM record, and notify the support team.',
      intent: 'Process inbound customer requests',
    };

    try {
      const response = await fetch(`${API_BASE_URL}/workflows`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(workflowPayload),
      });

      if (response.ok) {
        await loadData();
      }
    } catch (error) {
      console.error('Failed to create workflow:', error);
    }
  };

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">AI Workflow Automation</p>
          <h1>WorkFlowOS</h1>
        </div>
        <button className="primary-btn" onClick={discoverWorkflow}>
          Discover Workflow
        </button>
      </header>

      <main className="content">
        <section className="hero-card">
          <div>
            <p className="label">Observed intent</p>
            <h2>Process Customer Request</h2>
            <p>
              WorkFlowOS identifies recurring digital work and converts it into an approved,
              automatable workflow using the most reliable execution path available.
            </p>
          </div>
          <div className="stats-grid">
            <div>
              <strong>{loading ? '…' : workflows.length}</strong>
              <span>Workflows</span>
            </div>
            <div>
              <strong>{patterns[0]?.confidence ? `${Math.round(patterns[0].confidence * 100)}%` : '—'}</strong>
              <span>Confidence</span>
            </div>
            <div>
              <strong>{patterns.length}</strong>
              <span>Patterns</span>
            </div>
          </div>
        </section>

        <section className="workflow-list">
          {patterns.map((pattern) => (
            <article key={pattern.name} className="workflow-card highlight-card">
              <div className="workflow-header">
                <h3>{pattern.name}</h3>
                <span className="status active">{pattern.status}</span>
              </div>
              <p>{pattern.description}</p>
              <div className="meta-row">
                <span>Sources</span>
                <strong>{pattern.sources.join(' → ')}</strong>
              </div>
            </article>
          ))}

          {workflows.length === 0 && !loading && (
            <article className="workflow-card empty-card">
              <h3>No workflows discovered yet</h3>
              <p>Open the desktop agent or create a workflow to begin learning recurring actions.</p>
            </article>
          )}

          {workflows.map((workflow) => (
            <article key={workflow.workflow_id || workflow.name} className="workflow-card">
              <div className="workflow-header">
                <h3>{workflow.name}</h3>
                <span className={`status ${(workflow.status || 'draft').toLowerCase()}`}>
                  {workflow.status || 'Draft'}
                </span>
              </div>
              <p>{workflow.description}</p>
              <div className="meta-row">
                <span>Intent</span>
                <strong>{workflow.intent}</strong>
              </div>
            </article>
          ))}
        </section>
      </main>
    </div>
  );
}
