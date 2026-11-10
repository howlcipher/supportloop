# Prior art and unresolved opportunity

Research date: November 8, 2026. These primary sources document capabilities;
they do not demonstrate independently measured accuracy or unmet demand.

| Source | Documented overlap |
| --- | --- |
| [Zendesk categories](https://support.zendesk.com/hc/en-us/articles/7043747123354-Understanding-autoscoring-categories) and [custom QA](https://www.zendesk.com/service/quality-assurance/) | Solution-offered and comprehension checks, configurable QA; vendor marketing also advertises conversation-loop detection |
| [Intercom definitions](https://www.intercom.com/help/en/articles/7022438-reporting-metrics-attributes) | Answered, assumed-resolution and confirmed-resolution distinctions |
| [Salesforce methodology](https://www.salesforce.com/agentforce/use-cases/customer-zero/how-salesforce-measures-answer-quality/) | Relevance, correctness, completeness, synthetic inputs and acceptance criteria |
| [ServiceNow Conversation Insights](https://www.servicenow.com/docs/r/intelligent-experiences/conversational-intelligence/exploring-conversation-insights.html) | Resolution, effort, confusion, next steps and escalation analysis |
| [Jira reopening](https://support.atlassian.com/jira/kb/limit-customer-issue-reopening-to-x-days-after-resolution/) | Configurable reopening workflow |
| [Cresta QA](https://cresta.com/cresta-quality-management) | Outcome inference including resolution |
| [EvaluAgent API](https://docs.evaluagent.com/) | Evaluation results and policy-context document management |
| [Chatwoot Captain reports](https://www.chatwoot.com/hc/user-guide/articles/1791891433-captain-overview-and-reports) | Reopening and seven-day closure persistence |
| [Zammad 7.0](https://zammad.com/en/product/releases/7-0) | AI summaries of customer intent/open questions, writing assistance and role-based reporting profiles |
| [ResolveAI](https://github.com/Obumezi/ResolveAI) | Adjacent prototype describing deterministic verification of proposed IT diagnoses; README inspected, implementation not evaluated |

## Hypotheses to challenge

The broad feature list overlaps established QA. Possible differentiation is
local, vendor-independent, inspectable auditing from exports with uncertainty
and evidence boundaries. This combination is not established as novel.
No-match in a search cannot establish absence. This survey is not exhaustive.

Potential users include support engineers, independent QA reviewers and teams
using several help desks. No interviews, purchasing evidence or adoption data
exist here. Customer-side analysis cannot establish internal investigation or
compel a vendor to act. Organizational incentives may dominate tooling limits.

Compare an existing configured rubric before claiming a product gap. If it
meets users' privacy, portability and review needs, prefer configuration or a
small integration. An open benchmark or rubric can remain a useful engineering
artifact even if the commercial product premise fails.

## Audit clarification: November 10, 2026 UTC

The linked primary pages were revisited during the comprehensive audit.
Zendesk's solution-offered category checks whether a solution was proposed;
it is not evidence that the remedy executed. Its QA marketing also advertises
stuck-conversation-loop detection, making circular-referral detection an overlap
to compare rather than an assumed novelty. Intercom explicitly distinguishes
assumed and confirmed resolution, while Chatwoot documents reopening and
seven-day closure persistence. These remain product definitions and vendor
claims, not a same-input benchmark or proof of real-world resolution.

Zammad's release page specifically documents customer intent and open questions
in summaries, plus reporting-profile access controls. These are adjacent to the
proposed objective/question tracking. ServiceNow's official indexed documentation
supports the listed inferred signals; the browser fetch intermittently failed,
so this audit does not claim an independently archived page capture. The survey
still cannot establish exhaustive market coverage or configured-product adequacy.
