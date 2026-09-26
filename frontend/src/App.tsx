const workflowExamples = [
  {
    name: 'Process Customer Request',
    description: 'Read the email, update the CRM, and notify the support team.',
    status: 'Approved',
    intent: 'Handle inbound customer issues',
  },
  {
    name: 'Weekly Reporting',
    description: 'Collect metrics, update Excel, and send status summary to leadership.',
    status: 'Draft',
    intent: 'Prepare internal weekly reporting',
  },
  {
    name: 'Document Intake',
    description: 'Capture uploaded documents, classify them, and save to the right folder.',
    status: 'Active',
    intent: 'Automate document triage',
  },
];

export default function App() {
  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">AI Workflow Automation</p>
          <h1>WorkFlowOS</h1>
        </div>
        <button className="primary-btn">Discover Workflow</button>
      </header>

      <main className="content">
        <section className="hero-card">
          <div>
            <p className="label">Observed intent</p>
            <h2>Process Customer Request</h2>
            <p>
              WorkFlowOS identified a repeating pattern across Gmail, the CRM, and Slack
              and generated a suggested automation workflow.
            </p>
          </div>
          <div className="stats-grid">
            <div>
              <strong>14</strong>
              <span>Events captured</span>
            </div>
            <div>
              <strong>92%</strong>
              <span>Confidence</span>
            </div>
            <div>
              <strong>3</strong>
              <span>Patterns detected</span>
            </div>
          </div>
        </section>

        <section className="workflow-list">
          {workflowExamples.map((workflow) => (
            <article key={workflow.name} className="workflow-card">
              <div className="workflow-header">
                <h3>{workflow.name}</h3>
                <span className={`status ${workflow.status.toLowerCase()}`}>{workflow.status}</span>
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
