import Image from 'next/image'
import { faBorderAll, faGear } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { SideBarNavDrawer } from './SideBarItems'
import {
  MageDashboardFill,
  MaterialSymbolsSettingsOutline,
} from '@/components/ui/icons'

const dashboardItems = [
  { name: 'Messages', link: '/dashboard/messages' },
  { name: 'Tasks', link: '/dashboard/tasks' },
  {
    name: 'Inbox',
    link: '/dashboard/inbox',
  },
]

const processItems = [
  { name: 'Create new', link: '/process/create' },
  { name: 'Edit', link: '/process/edit' },
]

const SideBar = () => {
  return (
    <div className="h-screen w-[20%] sticky top-0 left-0 py-3 px-4 bg-overlay border-r-1 space-y-10">
      <Image
        src={'/images/mainLogo.png'}
        alt="Hirasys Logo"
        width={180}
        height={200}
      />
      <div className="space-y-3 ">
        <SideBarNavDrawer
          title="Dashboard"
          link="/dashboard"
          items={dashboardItems}
          icon={<MageDashboardFill width={'1.2rem'} height={'1.2rem'} />}
        />

        <SideBarNavDrawer
          title="Processes"
          link="/process"
          items={processItems}
          icon={
            <MaterialSymbolsSettingsOutline
              width={'1.2rem'}
              height={'1.2rem'}
            />
          }
        />
      </div>
    </div>
  )
}

export default SideBar
